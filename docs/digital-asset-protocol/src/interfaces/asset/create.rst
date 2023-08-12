src/interfaces/asset/create.rs
==============================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::collections::{BTreeMap};
use bebop::SliceWrapper;
use solana_program::account_info::AccountInfo;
use crate::api::{DigitalAssetProtocolError};
use crate::interfaces::ContextAction;
use crate::lifecycle::Lifecycle;
use crate::module::{ModuleDataWrapper};
use crate::blob::Asset;
use crate::generated::schema::owned::{
    Authority,
    ModuleData,
    ModuleType,
    OwnershipModel,
    RoyaltyModel,
    RoyaltyTarget,
    JsonDataSchema,
    Creator,
    ActionData,
    DataItemValue,
};
use crate::required_field;
use crate::validation::validate_creator_shares;

pub struct CreateV1<'info> {
    pub id: AccountInfo<'info>,
    pub owner: AccountInfo<'info>,
    pub payer: AccountInfo<'info>,
    pub creators: Vec<Creator>,
    pub ownership_model: OwnershipModel,
    pub authorities: Vec<Authority>,
    pub royalty_model: RoyaltyModel,
    pub royalty_target: Option<RoyaltyTarget>,
    pub off_chain_schema: JsonDataSchema,
    pub uri: String,
}

impl<'info> CreateV1<'info> {
    pub fn new(accounts: &[AccountInfo<'info>], action: ActionData) -> Result<(Self, usize), DigitalAssetProtocolError> {
        if let ActionData::CreateAssetV1 {
            uri,
            data_schema,
            royalty_model,
            royalty_target,
            ownership_model,
            creator_shares, // in percentage,
            authorities,
            ..
        } = action {
            // Need program id System program,
            let program = accounts[0].clone();
            let system = accounts[1].clone();
            let rent = accounts[2].clone();
            let id = accounts[3].clone();
            let owner = accounts[4].clone();
            let payer = accounts[5].clone();
            let payer_authority = payer.clone();
            let shares: Vec<u8> = required_field!(creator_shares)?;
            let creators = &accounts[6..accounts.len()];
            let remaining_accounts_index = 6 + creators.len();
            validate_creator_shares(creators, &shares)?;
            let creator_list = creators.iter().enumerate().map(|(i, ai)| {
                let verified = ai.is_signer;
                Creator {
                    address: ai.key.to_bytes().to_vec(),
                    share: shares[i],
                    verified,
                }
            }).collect();
            let uri = required_field!(uri)?.to_string();
            let ownership_model = required_field!(ownership_model)?;
            let royalty_model = required_field!(royalty_model)?;
            let royalty_target = royalty_target;

            return Ok((
                CreateV1 {
                    id,
                    owner,
                    payer,
                    creators: creator_list,
                    ownership_model,
                    authorities: authorities.unwrap_or(vec![Authority {
                        scopes: vec![
                            "*".to_string()
                        ],
                        address: payer_authority.key.to_bytes().to_vec(),
                    }]),
                    royalty_model,
                    royalty_target,
                    off_chain_schema: data_schema.unwrap_or(JsonDataSchema::Core),
                    uri: uri.to_string(),
                },
                remaining_accounts_index
            ));
        }
        Err(DigitalAssetProtocolError::ActionError("Invalid Action format, action must be CreateAssetV1".to_string()))
    }
}

impl<'info> ContextAction for CreateV1<'info> {
    fn lifecycle(&self) -> &Lifecycle {
        &Lifecycle::Create
    }

    fn run(&self) -> Result<(), DigitalAssetProtocolError> {
        let mut data = self.id.try_borrow_mut_data().map_err(|_| {
            DigitalAssetProtocolError::ActionError("Issue with Borrowing Data".to_string())
        })?;
        let modules = vec![
            ModuleType::Data,
            ModuleType::Ownership,
            ModuleType::Creators,
            ModuleType::Royalty,
            ModuleType::Governance,
            ModuleType::Rights,
            ModuleType::Extension,
        ];
        let mut new_asset = Asset::new();
        let owner_key = self.owner.key.to_bytes();
        for m in modules {
            let processor = ModuleType::to_processor(m);
            let data: Option<ModuleDataWrapper> = match m {
                ModuleType::Ownership => {
                    Some(ModuleDataWrapper::Structured(ModuleData::OwnershipData {
                        model: OwnershipModel::Single,
                        owner: owner_key.to_vec(),
                    }))
                }
                ModuleType::Data => {
                    let mut data: BTreeMap<String, DataItemValue> = BTreeMap::new();
                    data.insert("uri".to_string(), DataItemValue::String { value: Some(self.uri.clone()) });
                    data.insert("schema".to_string(), DataItemValue::Int { value: Some(self.off_chain_schema as i32) });
                    Some(
                        ModuleDataWrapper::Unstructured(data)
                    )
                }
                _ => {
                    None
                }
            };
            let data = data.ok_or(DigitalAssetProtocolError::ActionError("Unknown Error".to_string()))?;
            new_asset.set_module(m, data);
            processor.create(&mut new_asset)?;
        }
        //Save asset
        new_asset.save(data)?;
        Ok(())
    }
}




