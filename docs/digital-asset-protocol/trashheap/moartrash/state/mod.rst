trashheap/moartrash/state/mod.rs
================================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    
mod standards;
mod asset;

pub use standard::*;
pub use actions::*;
pub use standards::*;
pub use blob::*;
pub use asset::*;




;

// pub trait Shizzle {
//     fn keys(&self) -> Vec<&u32> ;
//     fn get_thing(&self, id: ModuleType) -> Option<&Module> ;
//     fn set_thing(&mut self, id: ModuleType, m: Module) -> () ;
// }
// 
// impl Shizzle for Asset {
//     fn keys(&self) -> Vec<&u32>  {
//         self.layout.keys().into_iter().collect::<Vec<&u32>>()
//     }
// 
//     fn get_thing(&self, id: ModuleType) -> Option<&Module> {
//         self.layout.get(&(id as u32))
//     }
// 
//     fn set_thing(&mut self, id: ModuleType, m: Module) -> () {
//         self.layout.insert(id as u32, m);
//     }
// }
// 
// pub struct CreateNFTContext {
//     address: AccountInfo,
//     owner: AccountInfo,
//     payer: AccountInfo,
//     authority: AccountInfo,
//     remaining_accounts: Vec<AccountInfo>,
// }
// 
// impl CreateNFTContext {
//     fn validate(&self) -> Result<(), DigitalAssetProtocolError> {
//         if !self.payer.is_signer {
//             return Err(DigitalAssetProtocolError::ActionError("Payer must sign".to_string()));
//         }
//         Ok(())
//     }
//     fn act(
//         &self,
//         asset: & mut Asset,
//     ) -> Result<&Asset, DigitalAssetProtocolError> {
//         : for ind in asset.keys() {
//             let id = ModuleType::try_from(*ind).map_err(|e| {
//                 DigitalAssetProtocolError::ActionError(e.to_string())
//             })?;
//             match id {
//                 // ModuleType::Ownership => {
//                 //     create_ownership(self, asset_new)
//                 // }
//                 ModuleType::Royalty => {
//                     create_royalty(self, asset)
//                 }
//                 // ModuleType::Creators => {
//                 //     create_creators(self, asset_new)
//                 // }
//                 _ => Err(DigitalAssetProtocolError::ActionError(
//                     "Not Implemented".to_string(),
//                 )),
//             }?;
//         }
// 
//         Ok(&asset)
//     }
// }
// 
// //
// // fn create_ownership(
// //     ctx: &CreateNFTContext,
// //     asset: & mut Asset,
// // ) -> Result<& mut Asset, DigitalAssetProtocolError> {
// //     // validation of create ownership specific stuff
// //     let Some(Module::Ownership { model, owner }) =
// //         asset.layout.get(&(ModuleType::Ownership as u32));
// //     if *model == OwnershipModel::Token && ctx.owner.owner != &spl_token::id() {
// //         return Err(DigitalAssetProtocolError::ModuleError(
// //             "Token Owner must be a Mint".to_string(),
// //         ));
// //     }
// //     Ok(asset)
// // }
// //
// fn create_royalty(
//     ctx: &CreateNFTContext,
//     asset: & mut Asset,
// ) -> Result<& mut Asset, DigitalAssetProtocolError> {
//     // validation of create ownership specific stuff
//     let module_data = asset.get_thing(ModuleType::Royalty);
//     if let Some(Module::Royalty {
//                     model,
//                     target,
//                     royalty_percent,
//                     locked
//                 }) = module_data {
//         let creators_model = *model == RoyaltyModel::Creators;
//         let creator_module = asset.get_thing(ModuleType::Creators);
//         if creators_model && creator_module.is_none() {
//             return Err(DigitalAssetProtocolError::ModuleError(
//                 "Creators Must be set".to_string(),
//             ));
//         }
//         let target = if creators_model && !target.is_empty() {
//             Vec::default()
//         } else {
//             target.clone()
//         };
//         asset.set_thing(ModuleType::Royalty, Module::Royalty {
//             model: *model,
//             target,
//             royalty_percent: 100,
//             locked: false,
//         });
//     } else {
//         return Err(DigitalAssetProtocolError::ModuleError(
//             "1 or more creators must be present".to_string(),
//         ));
//     }
//     Ok(asset)
// }
// 
// // fn create_creators(
// //     ctx: &CreateNFTContext,
// //     asset: & mut Asset,
// // ) -> Result<& mut Asset, DigitalAssetProtocolError> {
// //     let module_data = asset.layout.get(&(ModuleType::Creators as u32));
// //     if module_data.is_none() {
// //         return Err(DigitalAssetProtocolError::ModuleError(
// //             "1 or more creators must be present".to_string(),
// //         ));
// //     }
// //     let Module::Creators { creator_list } = module_data.unwrap();
// //
// //     if creator_list.is_empty() {
// //         return Err(DigitalAssetProtocolError::ModuleError(
// //             "1 or more creators must be present".to_string(),
// //         ));
// //     }
// //     Ok(asset)
// // }

