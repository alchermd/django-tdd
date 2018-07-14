# Improving Functional Tests: Ensuring Isolation and Removing Voodoo Sleeps

There are still a couple of issues:

1.  The functional tests doesn't clean up themselves (results are saved, failing subsequent tests).
2.  `time.sleep`s are still used.

We fix issue #1 by using Django's own `LiveServerTestCase` instead of the `unittest.TestCase`.

```python
from django.test import LiveServerTestCase

class TestFooBar(LiveServerTestCase):
    # ...
```

This way, Django will handle the functional test the same way as the unit tests.

As for issue #2, we write a custom retry/polling logic to time our tests:

```python
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

# inside our tests...
start_time = time.time()

while True:
    try:
        # Run the assertions ...
        return
    except (AssertionError, WebDriverException) as e:
        if time.time() - start_time > MAX_WAIT:
            raise e
        time.sleep(0.5)
```
