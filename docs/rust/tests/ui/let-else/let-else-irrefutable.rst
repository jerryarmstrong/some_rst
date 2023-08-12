tests/ui/let-else/let-else-irrefutable.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    let x = 1 else { return }; //~ WARN irrefutable `let...else` pattern

    // Multiline else blocks should not get printed
    let x = 1 else { //~ WARN irrefutable `let...else` pattern
        eprintln!("problem case encountered");
        return
    };
}


