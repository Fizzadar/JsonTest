# JsonTest

`JsonTest` is a tiny metaclass designed for automatically generating tests based off JSON files. Originally built for testing [`ElasticQuery`](https://github.com/Fizzadar/ElasticQuery). Install with `pip install jsontest`.

## Synopsis

```py
from jsontest import JsonTest

class MyTests(TestCase):
    # Set the metaclass to JsonTest
    __metaclass__ = JsonTest

    # Tell JsonTest where to find our JSON files
    jsontest_files = path.join('tests', 'filters')

    # Optional prefix for the test names
    jsontest_prefix = 'test_'

    # Define a function to run against each file
    def jsontest_function(self, test_name, test_data):
        print(test_name, test_data)
        self.assertFalse(False)
```
