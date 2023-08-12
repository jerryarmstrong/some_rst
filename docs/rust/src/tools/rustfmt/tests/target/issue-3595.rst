src/tools/rustfmt/tests/target/issue-3595.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct ReqMsg();
struct RespMsg();

pub type TestType = fn() -> (ReqMsg, fn(RespMsg) -> ());


