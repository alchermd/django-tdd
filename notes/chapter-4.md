# What Are We Doing with All These Tests? (And, Refactoring)

- _Test-Driven Development_ is a long term investment.
- Instead of doing guesswork when your _code is complex enough_ to be tested, why not do it from the start?
- "_One of the great things about TDD is that you never have to worry about forgetting what to do next—​just rerun your tests and they will tell you what you need to work on._"
- Don't test constants! Unit tests are for testing logic, flow control, and configuration.

```python
# Asserting <html> ....
self.assertTrue(html.startswith('<html>'))
self.assertIn('<title>Task Manager</title>', html)
self.assertTrue(html.endswith('</html>'))
```

What exactly are we doing here? In the end, we just want to make sure that the correc HTML file (a template) is being loaded. So let's test that instead!

```python
response = self.client.get('/')
self.assertTemplateUsed(response, 'index.html')
```

- On refactoring:

> When refactoring, work on either the code or the tests, but not both at once.
