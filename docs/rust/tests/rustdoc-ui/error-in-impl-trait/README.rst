tests/rustdoc-ui/error-in-impl-trait/README.md
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    Each of these needs to be in a separate file,
because the `delay_span_bug` ICE in rustdoc won't be triggerred
if even a single other error was emitted.

However, conceptually they are all testing basically the same thing.
See https://github.com/rust-lang/rust/pull/73566#issuecomment-653689128
for more details.


