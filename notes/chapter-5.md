# Saving User Input: Testing the Database

- Django has a builtin security fo CSRF exploit attempts. We use it like this:

```html
<form method="POST">
    {% csrf_token %}
    <!-- ... -->
</form>
```

- Red/Green/Refactor and Triangulation

1.  Write a unit test that fails (red)
2.  Write the simples implementation to make it pass (green)
3.  Refactor to make it better

What should be refactored? A good one is _duplication_ - if your implementation is _cheating_ to make the tests pass, it might be duplicating code _from your tests to your implementation_. Or better yet, write more tests that prevent you from cheating your code!

- Code appears three times? Refactor it out.
- Redirect after a `POST` request!
