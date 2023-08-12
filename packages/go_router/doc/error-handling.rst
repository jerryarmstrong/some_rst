packages/go_router/doc/error-handling.md
========================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: md

    By default, go_router comes with default error screens for both `MaterialApp`
and `CupertinoApp` as well as a default error screen in the case that none is
used. You can also replace the default error screen by using the
[errorBuilder](https://pub.dev/documentation/go_router/latest/go_router/GoRouter/GoRouter.html)
parameter:

```dart
GoRouter(
  /* ... */
  errorBuilder: (context, state) => ErrorScreen(state.error),
);
```


