from grpcalchemy.blueprint import Blueprint, Context
from grpcalchemy.client import Client
from grpcalchemy.orm import Message, StringField
from grpcalchemy.server import Server

from .test_grpcalchemy import TestGrpcalchemy


class TestServer(TestGrpcalchemy):
    def setUp(self):
        super().setUp()

        class TestMessage(Message):
            test_name = StringField()

        self.test_blueprint = Blueprint("test_blueprint")

        @self.test_blueprint.register
        def test_message(request: TestMessage,
                         context: Context) -> TestMessage:
            return TestMessage(test_name=request.test_name)

        self.test_message = test_message
        self.Message = TestMessage
        self.app = Server()
        self.app.register(self.test_blueprint)
        self.app.run(test=True)

    def tearDown(self):
        self.app.server.stop(0)

    def test_server(self):
        test_name = "Hello World!"
        with Client("localhost:50051") as client:
            client.register(self.test_blueprint)
            response = client.test_blueprint(
                rpc=self.test_message,
                message=self.Message(test_name=test_name))
            self.assertEqual(test_name, response.test_name)

    def test_server_listener(self):
        test_app = Server()

        @test_app.listener("before_server_start")
        def before_server_start(app: Server):
            pass

        def after_server_stop(app: Server):
            pass

        test_app.listener("after_server_stop", after_server_stop)

        self.assertListEqual([before_server_start],
                             test_app.listeners["before_server_start"])
        self.assertEqual([after_server_stop],
                         test_app.listeners["after_server_stop"])
