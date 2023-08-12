src/tools/rustfmt/tests/source/async_fn.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018

async fn bar() -> Result<(), ()> {
    Ok(())
}

pub async fn baz() -> Result<(), ()> {
    Ok(())
}

async unsafe fn foo() {
    async move {
        Ok(())
    }
}

async unsafe fn rust() {
    async move { // comment
        Ok(())
    }
}

async fn await_try() {
    something
     .await
      ?
     ;
}


