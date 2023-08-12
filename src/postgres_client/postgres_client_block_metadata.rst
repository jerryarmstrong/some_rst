src/postgres_client/postgres_client_block_metadata.rs
=====================================================

Last edited: 2023-06-03 03:13:41

Contents:

.. code-block:: rs

    use {
    crate::{
        geyser_plugin_postgres::{GeyserPluginPostgresConfig, GeyserPluginPostgresError},
        postgres_client::{
            postgres_client_transaction::DbReward, SimplePostgresClient, UpdateBlockMetadataRequest,
        },
    },
    chrono::Utc,
    log::*,
    postgres::{Client, Statement},
    solana_geyser_plugin_interface::geyser_plugin_interface::{
        GeyserPluginError, ReplicaBlockInfoV2,
    },
};

#[derive(Clone, Debug)]
pub struct DbBlockInfo {
    pub slot: i64,
    pub blockhash: String,
    pub rewards: Vec<DbReward>,
    pub block_time: Option<i64>,
    pub block_height: Option<i64>,
}

impl<'a> From<&ReplicaBlockInfoV2<'a>> for DbBlockInfo {
    fn from(block_info: &ReplicaBlockInfoV2) -> Self {
        Self {
            slot: block_info.slot as i64,
            blockhash: block_info.blockhash.to_string(),
            rewards: block_info.rewards.iter().map(DbReward::from).collect(),
            block_time: block_info.block_time,
            block_height: block_info
                .block_height
                .map(|block_height| block_height as i64),
        }
    }
}

impl SimplePostgresClient {
    pub(crate) fn build_block_metadata_upsert_statement(
        client: &mut Client,
        config: &GeyserPluginPostgresConfig,
    ) -> Result<Statement, GeyserPluginError> {
        let stmt =
            "INSERT INTO block (slot, blockhash, rewards, block_time, block_height, updated_on) \
        VALUES ($1, $2, $3, $4, $5, $6) \
        ON CONFLICT (slot) DO UPDATE SET blockhash=excluded.blockhash, rewards=excluded.rewards, \
        block_time=excluded.block_time, block_height=excluded.block_height, updated_on=excluded.updated_on";

        let stmt = client.prepare(stmt);

        match stmt {
            Err(err) => {
                Err(GeyserPluginError::Custom(Box::new(GeyserPluginPostgresError::DataSchemaError {
                    msg: format!(
                        "Error in preparing for the block metadata update PostgreSQL database: ({}) host: {:?} user: {:?} config: {:?}",
                        err, config.host, config.user, config
                    ),
                })))
            }
            Ok(stmt) => Ok(stmt),
        }
    }

    pub(crate) fn update_block_metadata_impl(
        &mut self,
        block_info: UpdateBlockMetadataRequest,
    ) -> Result<(), GeyserPluginError> {
        let client = self.client.get_mut().unwrap();
        let statement = &client.update_block_metadata_stmt;
        let client = &mut client.client;
        let updated_on = Utc::now().naive_utc();

        let block_info = block_info.block_info;
        let result = client.query(
            statement,
            &[
                &block_info.slot,
                &block_info.blockhash,
                &block_info.rewards,
                &block_info.block_time,
                &block_info.block_height,
                &updated_on,
            ],
        );

        if let Err(err) = result {
            let msg = format!(
                "Failed to persist the update of block metadata to the PostgreSQL database. Error: {:?}",
                err);
            error!("{}", msg);
            return Err(GeyserPluginError::AccountsUpdateError { msg });
        }

        Ok(())
    }
}


