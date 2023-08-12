src/tools/rustfmt/tests/source/match-block-trailing-comma.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-match_block_trailing_comma: true
// Match expressions, no unwrapping of block arms or wrapping of multiline
// expressions.

fn foo() {
    match x {
        a => {
            "line1";
            "line2"
        }
        ThisIsA::Guard if true => {
            "line1";
            "line2"
        }
        ThisIsA::ReallyLongPattern(ThatWillForce::TheGuard, ToWrapOnto::TheFollowingLine) if true => {
            "line1";
            "line2"
        }
        b => (aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,
              bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb),
    }
}


