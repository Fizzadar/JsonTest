import json
from os import listdir, path


class JsonTest(type):
    def __init__(cls, *args, **kwargs):
        # Get the JSON files
        files = listdir(cls.jsontest_files)
        files = [f for f in files if f.endswith('.json')]

        # Loop them and create class methods to call the jsontest_function
        for filename in files:
            test_name = 'test_{0}'.format(filename[:-5])
            test_data = json.loads(open(path.join(cls.jsontest_files, filename)).read())

            # We have to define a local method, lambda doesn't seem to work with nose
            def test(self):
                self.jsontest_function(test_data)

            setattr(cls, test_name, test)

        return super(JsonTest, cls).__init__(*args, **kwargs)
