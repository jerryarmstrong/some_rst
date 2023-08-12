tests/ui/closures/issue-82438-mut-without-upvar.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::error::Error;
struct A {
}

impl A {
    pub fn new() -> A {
        A {
        }
    }

    pub fn f<'a>(
        &'a self,
        team_name: &'a str,
        c: &'a mut dyn FnMut(String, String, u64, u64)
    ) -> Result<(), Box<dyn Error>> {
        Ok(())
    }
}


fn main() {
    let A = A::new();
    let participant_name = "A";

    let c = |a, b, c, d| {};

    A.f(participant_name, &mut c); //~ ERROR cannot borrow
}


