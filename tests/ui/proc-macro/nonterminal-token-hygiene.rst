tests/ui/proc-macro/nonterminal-token-hygiene.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that marks from declarative macros are applied to tokens in nonterminal.

// check-pass
// compile-flags: -Z span-debug -Z macro-backtrace -Z unpretty=expanded,hygiene
// compile-flags: -Z trim-diagnostic-paths=no
// normalize-stdout-test "\d+#" -> "0#"
// normalize-stdout-test "expn\d{3,}" -> "expnNNN"
// aux-build:test-macros.rs

#![feature(decl_macro)]

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use]
extern crate test_macros;

macro_rules! outer {
    ($item:item) => {
        macro inner() {
            print_bang! { $item }
        }

        inner!();
    };
}

struct S;

outer! {
    struct S; // OK, not a duplicate definition of `S`
}

fn main() {}


