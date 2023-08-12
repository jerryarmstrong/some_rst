tests/ui/dropck/drop-with-active-borrows-2.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn read_lines_borrowed<'a>() -> Vec<&'a str> {
    let raw_lines: Vec<String> = vec!["foo  ".to_string(), "  bar".to_string()];
    raw_lines.iter().map(|l| l.trim()).collect()
    //~^ ERROR cannot return value referencing local variable `raw_lines`
}

fn main() {
    println!("{:?}", read_lines_borrowed());
}


