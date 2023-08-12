tests/ui/tuple/wrong_argument_ice-3.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Process;

pub type Group = (Vec<String>, Vec<Process>);

fn test(process: &Process, groups: Vec<Group>) -> Vec<Group> {
    let new_group = vec![String::new()];

    if groups.capacity() == 0 {
        groups.push(new_group, vec![process]);
        //~^ ERROR this method takes 1 argument but 2 arguments were supplied
        return groups;
    }

    todo!()
}

fn main() {}


