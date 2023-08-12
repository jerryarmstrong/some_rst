compiler/rustc_const_eval/src/util/collect_writes.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use rustc_middle::mir::visit::PlaceContext;
use rustc_middle::mir::visit::Visitor;
use rustc_middle::mir::{Body, Local, Location};

pub trait FindAssignments {
    // Finds all statements that assign directly to local (i.e., X = ...)
    // and returns their locations.
    fn find_assignments(&self, local: Local) -> Vec<Location>;
}

impl<'tcx> FindAssignments for Body<'tcx> {
    fn find_assignments(&self, local: Local) -> Vec<Location> {
        let mut visitor = FindLocalAssignmentVisitor { needle: local, locations: vec![] };
        visitor.visit_body(self);
        visitor.locations
    }
}

// The Visitor walks the MIR to return the assignment statements corresponding
// to a Local.
struct FindLocalAssignmentVisitor {
    needle: Local,
    locations: Vec<Location>,
}

impl<'tcx> Visitor<'tcx> for FindLocalAssignmentVisitor {
    fn visit_local(&mut self, local: Local, place_context: PlaceContext, location: Location) {
        if self.needle != local {
            return;
        }

        if place_context.is_place_assignment() {
            self.locations.push(location);
        }
    }
}


