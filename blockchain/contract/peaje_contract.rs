#![cfg_attr(not(feature = "std"), no_std)]

#[ink::contract]
mod peaje_contract {
    use ink_storage::collections::Mapping;
    use ink_prelude::vec::Vec;

    #[ink(storage)]
    pub struct PeajeContract {
        tarifas: Mapping<u32, u128>,
        pagos: Mapping<(AccountId, u32), u128>,
    }

    impl PeajeContract {
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                tarifas: Mapping::new(),
                pagos: Mapping::new(),
            }
        }

        #[ink(message)]
        pub fn establecer_tarifa(&mut self, peaje_id: u32, tarifa: u128) {
            self.tarifas.insert(peaje_id, &tarifa);
        }

        #[ink(message, payable)]
        pub fn pagar_peaje(&mut self, peaje_id: u32) {
            let caller = self.env().caller();
            let pago = self.env().transferred_value();
            let tarifa = self.tarifas.get(&peaje_id).unwrap_or(0);

            assert!(pago >= tarifa, "Fondos insuficientes para el peaje");

            self.pagos.insert((caller, peaje_id), &pago);
        }

        #[ink(message)]
        pub fn obtener_tarifa(&self, peaje_id: u32) -> u128 {
            self.tarifas.get(&peaje_id).unwrap_or(0)
        }

        #[ink(message)]
        pub fn historial_pagos(&self, usuario: AccountId) -> Vec<(u32, u128)> {
            let mut pagos = Vec::new();
            for (peaje_id, monto) in self.pagos.iter() {
                if peaje_id.0 == usuario {
                    pagos.push((peaje_id.1, *monto));
                }
            }
            pagos
        }
    }
}
