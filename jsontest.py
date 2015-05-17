import json
from os import listdir, path


class JsonTest(type):
    def __new__(cls, name, bases, attrs):
        # Get the JSON files
        files = listdir(attrs['jsontest_files'])
        files = [f for f in files if f.endswith('.json')]

        def gen_test(test_name, test_data):
            def test(self):
                self.jsontest_function(test_name, test_data)

            return test

        # Loop them and create class methods to call the jsontest_function
        for filename in files:
            test_name = filename[:-5]
            test_data = json.loads(open(path.join(attrs['jsontest_files'], filename)).read())

            # Attach the method
            method_name = 'test_{0}'.format(test_name)
            attrs[method_name] = gen_test(test_name, test_data)

        return type.__new__(cls, name, bases, attrs)
