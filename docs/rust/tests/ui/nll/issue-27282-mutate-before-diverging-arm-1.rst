tests/ui/nll/issue-27282-mutate-before-diverging-arm-1.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is testing an attempt to corrupt the discriminant of the match
// arm in a guard, followed by an attempt to continue matching on that
// corrupted discriminant in the remaining match arms.
//
// Basically this is testing that our new NLL feature of emitting a
// fake read on each match arm is catching cases like this.
//
// This case is interesting because it includes a guard that
// diverges, and therefore a single final fake-read at the very end
// after the final match arm would not suffice.

struct ForceFnOnce;

fn main() {
    let mut x = &mut Some(&2);
    let force_fn_once = ForceFnOnce;
    match x {
        &mut None => panic!("unreachable"),
        &mut Some(&_) if {
            // ForceFnOnce needed to exploit #27282
            (|| { *x = None; drop(force_fn_once); })();
            //~^ ERROR cannot mutably borrow `x` in match guard [E0510]
            false
        } => {}
        &mut Some(&a) if { // this binds to garbage if we've corrupted discriminant
            println!("{}", a);
            panic!()
        } => {}
        _ => panic!("unreachable"),
    }
}


