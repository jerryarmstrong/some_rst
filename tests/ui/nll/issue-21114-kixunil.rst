tests/ui/nll/issue-21114-kixunil.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn from_stdin(min: u64) -> Vec<u64> {
    use std::io::BufRead;

    let stdin = std::io::stdin();
    let stdin = stdin.lock();

    stdin.lines()
        .map(Result::unwrap)
        .map(|val| val.parse())
        .map(Result::unwrap)
        .filter(|val| *val >= min)
        .collect()
}

fn main() {}


