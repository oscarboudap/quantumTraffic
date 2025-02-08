#![cfg_attr(not(feature = "std"), no_std)]

#[frame_support::pallet]
pub mod pallet {
    use frame_support::{dispatch::DispatchResult, pallet_prelude::*};
    use frame_system::pallet_prelude::*;

    #[pallet::config]
    pub trait Config: frame_system::Config {
        type Event: From<Event<Self>> + IsType<<Self as frame_system::Config>::Event>;
    }

    #[pallet::storage]
    pub(super) type TarifaPeaje<T> = StorageMap<_, Blake2_128Concat, u32, u128, ValueQuery>;

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        TarifaEstablecida(u32, u128),
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        #[pallet::weight(10_000)]
        pub fn establecer_tarifa(origin: OriginFor<T>, peaje_id: u32, tarifa: u128) -> DispatchResult {
            let _who = ensure_signed(origin)?;
            TarifaPeaje::<T>::insert(peaje_id, tarifa);
            Self::deposit_event(Event::TarifaEstablecida(peaje_id, tarifa));
            Ok(())
        }
    }
}
