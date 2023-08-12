connector-mango/src/main.rs
===========================

Last edited: 2021-11-30 16:15:41

Contents:

.. code-block:: rs

    mod mango;

use {
    log::*,
    solana_accountsdb_connector_lib::*,
    std::{fs::File, io::Read, sync::Arc},
};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        println!("requires a config file argument");
        return Ok(());
    }

    let config: Config = {
        let mut file = File::open(&args[1])?;
        let mut contents = String::new();
        file.read_to_string(&mut contents)?;
        toml::from_str(&contents).unwrap()
    };

    solana_logger::setup_with_default("info");
    info!("startup");

    let account_tables: AccountTables = vec![
        Arc::new(RawAccountTable {}),
        Arc::new(mango::MangoAccountTable {}),
        Arc::new(mango::MangoGroupTable {}),
        Arc::new(mango::MangoCacheTable {}),
    ];

    let metrics_tx = metrics::start();

    let (account_write_queue_sender, slot_queue_sender) =
        postgres_target::init(&config.postgres_target, account_tables, metrics_tx.clone()).await?;

    info!("postgres done");
    let use_accountsdb = true;
    if use_accountsdb {
        grpc_plugin_source::process_events(
            config,
            account_write_queue_sender,
            slot_queue_sender,
            metrics_tx,
        )
        .await;
    } else {
        websocket_source::process_events(config, account_write_queue_sender, slot_queue_sender)
            .await;
    }

    Ok(())
}


