testsuite/cluster-test/src/effects/stop_container.rs
====================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use crate::{effects::Effect, instance::Instance};
use failure;
use std::fmt;

pub struct StopContainer {
    instance: Instance,
}

impl StopContainer {
    pub fn new(instance: Instance) -> Self {
        Self { instance }
    }
}

impl Effect for StopContainer {
    fn activate(&self) -> failure::Result<()> {
        self.instance
            .run_cmd(vec!["sudo /usr/sbin/service docker stop"])
    }

    fn deactivate(&self) -> failure::Result<()> {
        self.instance.run_cmd(vec![
            "sudo /usr/sbin/service docker start && sudo /usr/sbin/service ecs start",
        ])
    }
}

impl fmt::Display for StopContainer {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Stop container {}", self.instance)
    }
}


