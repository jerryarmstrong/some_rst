tests/ui/match/match-pattern-field-mismatch-2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    enum Color {
        Rgb(usize, usize, usize),
        Cmyk(usize, usize, usize, usize),
        NoColor,
    }

    fn foo(c: Color) {
        match c {
          Color::Rgb(_, _, _) => { }
          Color::Cmyk(_, _, _, _) => { }
          Color::NoColor(_) => { }
          //~^ ERROR expected tuple struct or tuple variant, found unit variant `Color::NoColor`
        }
    }
}


