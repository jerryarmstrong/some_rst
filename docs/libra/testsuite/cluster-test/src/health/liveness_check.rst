testsuite/cluster-test/src/health/liveness_check.rs
===================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use crate::{
    cluster::Cluster,
    health::{Event, HealthCheck, HealthCheckContext, ValidatorEvent},
};
use std::{collections::HashMap, time::Duration};

pub struct LivenessHealthCheck {
    last_committed: HashMap<String, LastCommitInfo>,
}

const MAX_BEHIND: Duration = Duration::from_secs(60);

#[derive(Default)]
struct LastCommitInfo {
    ve: Option<ValidatorEvent>,
    timestamp: Duration,
}

impl LivenessHealthCheck {
    pub fn new(cluster: &Cluster) -> Self {
        let mut last_committed = HashMap::new();
        for instance in cluster.instances() {
            last_committed.insert(instance.short_hash().clone(), LastCommitInfo::default());
        }
        Self { last_committed }
    }
}

impl HealthCheck for LivenessHealthCheck {
    fn on_event(&mut self, ve: &ValidatorEvent, ctx: &mut HealthCheckContext) {
        match ve.event {
            Event::Commit(..) => {
                if let Some(ref prev) = self.last_committed.get(&ve.validator) {
                    if prev.timestamp > ve.timestamp {
                        return;
                    }
                }
                self.last_committed.insert(
                    ve.validator.clone(),
                    LastCommitInfo {
                        ve: Some(ve.clone()),
                        timestamp: ve.timestamp,
                    },
                );
            }
            Event::ConsensusStarted => {
                ctx.report_failure(ve.validator.clone(), "validator restarted".into());
            }
        }
    }

    fn verify(&mut self, ctx: &mut HealthCheckContext) {
        let min_timestamp = ctx.now - MAX_BEHIND;
        for (validator, lci) in &self.last_committed {
            if lci.timestamp < min_timestamp {
                ctx.report_failure(
                    validator.clone(),
                    format!(
                        "Last commit is {} ms behind: {:?}",
                        (min_timestamp - lci.timestamp).as_millis(),
                        lci.ve,
                    ),
                );
            }
        }
    }

    fn invalidate(&mut self, validator: &str) {
        self.last_committed
            .insert(validator.into(), LastCommitInfo::default());
    }

    fn name(&self) -> &'static str {
        "liveness_check"
    }
}


