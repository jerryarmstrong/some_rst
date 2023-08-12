src/tools/rustfmt/tests/target/async_block.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018

fn main() {
    let x = async { Ok(()) };
}

fn baz() {
    // test
    let x = async {
        // async blocks are great
        Ok(())
    };

    let y = async { Ok(()) }; // comment

    spawn(a, async move {
        action();
        Ok(())
    });

    spawn(a, async move || {
        action();
        Ok(())
    });

    spawn(a, static async || {
        action();
        Ok(())
    });

    spawn(a, static async move || {
        action();
        Ok(())
    });
}


