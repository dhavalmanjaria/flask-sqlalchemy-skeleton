"""This function takes old-type RE assets and moves them to new RE assets

"""
from config import log
from data.real_estate_assets.real_estate_assets_models import INVESTMENT_TYPE
from data.real_estate_assets.real_estate_assets_utils import \
    find_single_re_asset_by_asset_id, add_real_estate_asset
from dtos.real_estate_assets.addAsset_real_estate_asset_dto import \
    AddAssetRealEstateAssetDTO
from psql import Asset, ASSET_CLASS, Transaction, User


def migrate_all_re_assets_for_user(user_id):

    all_re_assets_for_user = Asset.query.filter(
        Asset.user_id==user_id).filter(
        Asset.asset_class==ASSET_CLASS.RealEstate).all()

    for asset in all_re_assets_for_user:
        re_asset = find_single_re_asset_by_asset_id(asset.id)

        if not re_asset:
            # Old type asset
            # Then we migrate

            addAsset_dto = AddAssetRealEstateAssetDTO(
                name=asset.name,
                asset_class=asset.asset_class,
                asset_type=asset.asset_type,
                asset_currency=asset.asset_currency,
                remark=asset.remark,
                purchase_price=None,  # Don't need this here
                investment_type=INVESTMENT_TYPE.Other,
                market_value=None,  # Don't need this here
                value_date=None,  # Don't need this here
                purchase_date=None,  # Don't need this here
                location=None,  # Don't need this here
                upfront_costs=None,  # Don't need this here
                address=None,  # Don't need this here
                has_mortgage=False
            )

            new_re_asset, log_msg = add_real_estate_asset(
                asset=asset,
                addAssetWithREAsset_dto=addAsset_dto,
                commit=True
            )

            log.debug(log_msg)


def run_migrations_of_re_asset_for_all_users():
    users = User.query.all()

    for user in users:
        migrate_all_re_assets_for_user(user.id)


if __name__ == '__main__':
    run_migrations_of_re_asset_for_all_users()