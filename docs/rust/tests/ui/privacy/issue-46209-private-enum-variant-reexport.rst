tests/ui/privacy/issue-46209-private-enum-variant-reexport.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deny(unused_imports)]
mod rank {
    pub use self::Professor::*;
    //~^ ERROR glob import doesn't reexport anything
    pub use self::Lieutenant::{JuniorGrade, Full};
    //~^ ERROR `JuniorGrade` is private, and cannot be re-exported
    //~| ERROR `Full` is private, and cannot be re-exported
    pub use self::PettyOfficer::*;
    //~^ ERROR glob import doesn't reexport anything
    pub use self::Crewman::*;
    //~^ ERROR glob import doesn't reexport anything

    enum Professor {
        Adjunct,
        Assistant,
        Associate,
        Full
    }

    enum Lieutenant {
        JuniorGrade,
        Full,
    }

    pub(in rank) enum PettyOfficer {
        SecondClass,
        FirstClass,
        Chief,
        MasterChief
    }

    pub(crate) enum Crewman {
        Recruit,
        Apprentice,
        Full
    }

}

fn main() {}


