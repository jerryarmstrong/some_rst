tests/run-pass-valgrind/cleanup-stdin.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = std::io::stdin();
    let _ = std::io::stdout();
    let _ = std::io::stderr();
}


