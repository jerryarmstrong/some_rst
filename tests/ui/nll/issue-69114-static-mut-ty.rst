tests/ui/nll/issue-69114-static-mut-ty.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that borrowck ensures that `static mut` items have the expected type.

static FOO: u8 = 42;
static mut BAR: &'static u8 = &FOO;
static mut BAR_ELIDED: &u8 = &FOO;

fn main() {
    unsafe {
        println!("{} {}", BAR, BAR_ELIDED);
        set_bar();
        set_bar_elided();
        println!("{} {}", BAR, BAR_ELIDED);
    }
}

fn set_bar() {
    let n = 42;
    unsafe {
        BAR = &n;
        //~^ ERROR does not live long enough
    }
}

fn set_bar_elided() {
    let n = 42;
    unsafe {
        BAR_ELIDED = &n;
        //~^ ERROR does not live long enough
    }
}


