from selenium.webdriver.chrome.options import Options


class TestOptionsBuilder:
    """
    This class provides methods to build test options for running tests.

    Methods:
        - test_no_sandbox(builder): Adds '--no-sandbox' argument to the options.
        - test_no_screen(builder): Adds '--headless' argument to the options.
        - test_no_dev_shared_memory(builder): Adds '--disable-dev-shm-usage' argument to the options.
        - test_all_options_added(builder): Adds all available options to the builder.
        - test_build(builder): Builds and returns the options.

    Example Usage:
        builder = TestOptionsBuilder()
        builder.test_no_sandbox()
        options = builder.build()
    """
    def test_no_sandbox(self, builder):
        """
        :param builder: The original builder object.
        :return: None

        This method is used to test the `no_sandbox` method of the builder object. It verifies that the `no_sandbox`
        method properly sets the `builder_with_no_sandbox` object, and that the `builder` and `builder_with_no_sandbox`
        objects are equal. It also checks that the `builder_with_no_sandbox` object has the `arguments` attribute set to
        `['--no-sandbox']`.
        """
        builder_with_no_sandbox = builder.no_sandbox()
        assert builder == builder_with_no_sandbox
        assert builder_with_no_sandbox.options.arguments == ['--no-sandbox']

    def test_no_screen(self, builder):
        """
        :param builder: The current instance of the builder class.
        :return: None

        This method takes a builder object and sets the `no_screen` option to enable headless mode, which means the application will run without a visible screen. It asserts that the builder
        * object is equal to the one with `no_screen` option enabled and also asserts that the `arguments` attribute of the builder object is set to `['--headless']`.

        Example usage:

            builder = Builder()
            builder.no_screen()
            test_no_screen(builder)

        """
        builder_with_no_screen = builder.no_screen()
        assert builder == builder_with_no_screen
        assert builder_with_no_screen.options.arguments == ['--headless']

    def test_no_dev_shared_memory(self, builder):
        """
        :param builder: The builder instance to configure.
        :return: None

        This method tests the `no_dev_shared_memory` method of the builder class.
        It verifies that the `builder` instance is correctly updated with the option to disable dev shm usage.
        """
        builder_with_no_dev_shared_memory = builder.no_dev_shared_memory()
        assert builder == builder_with_no_dev_shared_memory
        assert builder_with_no_dev_shared_memory.options.arguments == ['--disable-dev-shm-usage']

    def test_all_options_added(self, builder):
        """
        Test if all options are added to the builder.

        :param builder: The Builder object to test.
        :return: None
        """
        builder_with_all_options = builder.no_dev_shared_memory().no_screen().no_sandbox()
        assert builder == builder_with_all_options
        assert builder_with_all_options.options.arguments == ['--disable-dev-shm-usage', '--headless', '--no-sandbox']

    def test_build(self, builder):
        """
        :param builder: The object used to build the options.
        :return: The built options object.
        """
        assert isinstance(builder.build(), Options)