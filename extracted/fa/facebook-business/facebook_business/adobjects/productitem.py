# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ProductItem(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductItem = True
        super(ProductItem, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_image_cdn_urls = 'additional_image_cdn_urls'
        additional_image_urls = 'additional_image_urls'
        additional_variant_attributes = 'additional_variant_attributes'
        age_group = 'age_group'
        applinks = 'applinks'
        availability = 'availability'
        brand = 'brand'
        bundle_items = 'bundle_items'
        bundle_retailer_ids = 'bundle_retailer_ids'
        capability_to_review_status = 'capability_to_review_status'
        category = 'category'
        category_specific_fields = 'category_specific_fields'
        color = 'color'
        commerce_insights = 'commerce_insights'
        condition = 'condition'
        currency = 'currency'
        custom_data = 'custom_data'
        custom_label_0 = 'custom_label_0'
        custom_label_1 = 'custom_label_1'
        custom_label_2 = 'custom_label_2'
        custom_label_3 = 'custom_label_3'
        custom_label_4 = 'custom_label_4'
        custom_number_0 = 'custom_number_0'
        custom_number_1 = 'custom_number_1'
        custom_number_2 = 'custom_number_2'
        custom_number_3 = 'custom_number_3'
        custom_number_4 = 'custom_number_4'
        description = 'description'
        errors = 'errors'
        expiration_date = 'expiration_date'
        fb_product_category = 'fb_product_category'
        gender = 'gender'
        generated_background_images = 'generated_background_images'
        generated_background_images_ad_usage = 'generated_background_images_ad_usage'
        gtin = 'gtin'
        id = 'id'
        image_cdn_urls = 'image_cdn_urls'
        image_fetch_status = 'image_fetch_status'
        image_url = 'image_url'
        images = 'images'
        importer_address = 'importer_address'
        importer_name = 'importer_name'
        invalidation_errors = 'invalidation_errors'
        inventory = 'inventory'
        is_bundle_hero = 'is_bundle_hero'
        manufacturer_info = 'manufacturer_info'
        manufacturer_part_number = 'manufacturer_part_number'
        marked_for_product_launch = 'marked_for_product_launch'
        material = 'material'
        mobile_link = 'mobile_link'
        name = 'name'
        ordering_index = 'ordering_index'
        origin_country = 'origin_country'
        parent_product_id = 'parent_product_id'
        pattern = 'pattern'
        post_conversion_signal_based_enforcement_appeal_eligibility = 'post_conversion_signal_based_enforcement_appeal_eligibility'
        price = 'price'
        product_catalog = 'product_catalog'
        product_feed = 'product_feed'
        product_group = 'product_group'
        product_local_info = 'product_local_info'
        product_relationship = 'product_relationship'
        product_type = 'product_type'
        quantity_to_sell_on_facebook = 'quantity_to_sell_on_facebook'
        retailer_id = 'retailer_id'
        retailer_product_group_id = 'retailer_product_group_id'
        review_rejection_reasons = 'review_rejection_reasons'
        review_status = 'review_status'
        sale_price = 'sale_price'
        sale_price_end_date = 'sale_price_end_date'
        sale_price_start_date = 'sale_price_start_date'
        shipping_weight_unit = 'shipping_weight_unit'
        shipping_weight_value = 'shipping_weight_value'
        short_description = 'short_description'
        size = 'size'
        start_date = 'start_date'
        tags = 'tags'
        url = 'url'
        vendor_id = 'vendor_id'
        video_fetch_status = 'video_fetch_status'
        videos = 'videos'
        visibility = 'visibility'
        wa_compliance_category = 'wa_compliance_category'
        android_app_name = 'android_app_name'
        android_class = 'android_class'
        android_package = 'android_package'
        android_url = 'android_url'
        checkout_url = 'checkout_url'
        commerce_tax_category = 'commerce_tax_category'
        ios_app_name = 'ios_app_name'
        ios_app_store_id = 'ios_app_store_id'
        ios_url = 'ios_url'
        ipad_app_name = 'ipad_app_name'
        ipad_app_store_id = 'ipad_app_store_id'
        ipad_url = 'ipad_url'
        iphone_app_name = 'iphone_app_name'
        iphone_app_store_id = 'iphone_app_store_id'
        iphone_url = 'iphone_url'
        launch_date = 'launch_date'
        product_priority_0 = 'product_priority_0'
        product_priority_1 = 'product_priority_1'
        product_priority_2 = 'product_priority_2'
        product_priority_3 = 'product_priority_3'
        product_priority_4 = 'product_priority_4'
        return_policy_days = 'return_policy_days'
        windows_phone_app_id = 'windows_phone_app_id'
        windows_phone_app_name = 'windows_phone_app_name'
        windows_phone_url = 'windows_phone_url'

    class AgeGroup:
        adult = 'adult'
        all_ages = 'all ages'
        infant = 'infant'
        kids = 'kids'
        newborn = 'newborn'
        teen = 'teen'
        toddler = 'toddler'

    class Availability:
        available_for_order = 'available for order'
        discontinued = 'discontinued'
        in_stock = 'in stock'
        mark_as_sold = 'mark_as_sold'
        out_of_stock = 'out of stock'
        pending = 'pending'
        preorder = 'preorder'

    class CapabilityToReviewStatus:
        approved = 'APPROVED'
        no_review = 'NO_REVIEW'
        outdated = 'OUTDATED'
        pending = 'PENDING'
        rejected = 'REJECTED'

    class Condition:
        cpo = 'cpo'
        new = 'new'
        open_box_new = 'open_box_new'
        refurbished = 'refurbished'
        used = 'used'
        used_fair = 'used_fair'
        used_good = 'used_good'
        used_like_new = 'used_like_new'

    class Gender:
        female = 'female'
        male = 'male'
        unisex = 'unisex'

    class ImageFetchStatus:
        direct_upload = 'DIRECT_UPLOAD'
        fetched = 'FETCHED'
        fetch_failed = 'FETCH_FAILED'
        no_status = 'NO_STATUS'
        outdated = 'OUTDATED'
        partial_fetch = 'PARTIAL_FETCH'

    class ReviewStatus:
        approved = 'approved'
        outdated = 'outdated'
        pending = 'pending'
        rejected = 'rejected'

    class ShippingWeightUnit:
        value_g = 'g'
        kg = 'kg'
        lb = 'lb'
        oz = 'oz'

    class VideoFetchStatus:
        direct_upload = 'DIRECT_UPLOAD'
        fetched = 'FETCHED'
        fetch_failed = 'FETCH_FAILED'
        no_status = 'NO_STATUS'
        outdated = 'OUTDATED'
        partial_fetch = 'PARTIAL_FETCH'

    class Visibility:
        published = 'published'
        staging = 'staging'

    class CommerceTaxCategory:
        fb_animal = 'FB_ANIMAL'
        fb_animal_supp = 'FB_ANIMAL_SUPP'
        fb_aprl = 'FB_APRL'
        fb_aprl_accessories = 'FB_APRL_ACCESSORIES'
        fb_aprl_athl_unif = 'FB_APRL_ATHL_UNIF'
        fb_aprl_cases = 'FB_APRL_CASES'
        fb_aprl_clothing = 'FB_APRL_CLOTHING'
        fb_aprl_costume = 'FB_APRL_COSTUME'
        fb_aprl_cstm = 'FB_APRL_CSTM'
        fb_aprl_formal = 'FB_APRL_FORMAL'
        fb_aprl_handbag = 'FB_APRL_HANDBAG'
        fb_aprl_jewelry = 'FB_APRL_JEWELRY'
        fb_aprl_shoe = 'FB_APRL_SHOE'
        fb_aprl_shoe_acc = 'FB_APRL_SHOE_ACC'
        fb_aprl_swim = 'FB_APRL_SWIM'
        fb_aprl_swim_chil = 'FB_APRL_SWIM_CHIL'
        fb_aprl_swim_cvr = 'FB_APRL_SWIM_CVR'
        fb_arts = 'FB_ARTS'
        fb_arts_hobby = 'FB_ARTS_HOBBY'
        fb_arts_party = 'FB_ARTS_PARTY'
        fb_arts_party_gift_card = 'FB_ARTS_PARTY_GIFT_CARD'
        fb_arts_ticket = 'FB_ARTS_TICKET'
        fb_baby = 'FB_BABY'
        fb_baby_bath = 'FB_BABY_BATH'
        fb_baby_blanket = 'FB_BABY_BLANKET'
        fb_baby_diaper = 'FB_BABY_DIAPER'
        fb_baby_gift_set = 'FB_BABY_GIFT_SET'
        fb_baby_health = 'FB_BABY_HEALTH'
        fb_baby_nursing = 'FB_BABY_NURSING'
        fb_baby_potty_trn = 'FB_BABY_POTTY_TRN'
        fb_baby_safe = 'FB_BABY_SAFE'
        fb_baby_toys = 'FB_BABY_TOYS'
        fb_baby_transport = 'FB_BABY_TRANSPORT'
        fb_baby_transport_acc = 'FB_BABY_TRANSPORT_ACC'
        fb_bags = 'FB_BAGS'
        fb_bags_bkpk = 'FB_BAGS_BKPK'
        fb_bags_boxes = 'FB_BAGS_BOXES'
        fb_bags_brfcs = 'FB_BAGS_BRFCS'
        fb_bags_csmt_bag = 'FB_BAGS_CSMT_BAG'
        fb_bags_dffl = 'FB_BAGS_DFFL'
        fb_bags_dipr = 'FB_BAGS_DIPR'
        fb_bags_fnny = 'FB_BAGS_FNNY'
        fb_bags_grmt = 'FB_BAGS_GRMT'
        fb_bags_lugg = 'FB_BAGS_LUGG'
        fb_bags_lug_acc = 'FB_BAGS_LUG_ACC'
        fb_bags_msgr = 'FB_BAGS_MSGR'
        fb_bags_tote = 'FB_BAGS_TOTE'
        fb_bags_trn_cas = 'FB_BAGS_TRN_CAS'
        fb_bldg = 'FB_BLDG'
        fb_bldg_acc = 'FB_BLDG_ACC'
        fb_bldg_cnsmb = 'FB_BLDG_CNSMB'
        fb_bldg_fence = 'FB_BLDG_FENCE'
        fb_bldg_fuel_tnk = 'FB_BLDG_FUEL_TNK'
        fb_bldg_ht_vnt = 'FB_BLDG_HT_VNT'
        fb_bldg_lock = 'FB_BLDG_LOCK'
        fb_bldg_matrl = 'FB_BLDG_MATRL'
        fb_bldg_plmb = 'FB_BLDG_PLMB'
        fb_bldg_pump = 'FB_BLDG_PUMP'
        fb_bldg_pwrs = 'FB_BLDG_PWRS'
        fb_bldg_str_tank = 'FB_BLDG_STR_TANK'
        fb_bldg_s_eng = 'FB_BLDG_S_ENG'
        fb_bldg_tl_acc = 'FB_BLDG_TL_ACC'
        fb_bldg_tool = 'FB_BLDG_TOOL'
        fb_busind = 'FB_BUSIND'
        fb_busind_advertising = 'FB_BUSIND_ADVERTISING'
        fb_busind_agriculture = 'FB_BUSIND_AGRICULTURE'
        fb_busind_automation = 'FB_BUSIND_AUTOMATION'
        fb_busind_heavy_mach = 'FB_BUSIND_HEAVY_MACH'
        fb_busind_lab = 'FB_BUSIND_LAB'
        fb_busind_medical = 'FB_BUSIND_MEDICAL'
        fb_busind_retail = 'FB_BUSIND_RETAIL'
        fb_busind_sanitary_ct = 'FB_BUSIND_SANITARY_CT'
        fb_busind_sign = 'FB_BUSIND_SIGN'
        fb_busind_storage = 'FB_BUSIND_STORAGE'
        fb_busind_storage_acc = 'FB_BUSIND_STORAGE_ACC'
        fb_busind_work_gear = 'FB_BUSIND_WORK_GEAR'
        fb_camera_acc = 'FB_CAMERA_ACC'
        fb_camera_camera = 'FB_CAMERA_CAMERA'
        fb_camera_optic = 'FB_CAMERA_OPTIC'
        fb_camera_optics = 'FB_CAMERA_OPTICS'
        fb_camera_photo = 'FB_CAMERA_PHOTO'
        fb_elec = 'FB_ELEC'
        fb_elec_acc = 'FB_ELEC_ACC'
        fb_elec_arcdade = 'FB_ELEC_ARCDADE'
        fb_elec_audio = 'FB_ELEC_AUDIO'
        fb_elec_circuit = 'FB_ELEC_CIRCUIT'
        fb_elec_comm = 'FB_ELEC_COMM'
        fb_elec_computer = 'FB_ELEC_COMPUTER'
        fb_elec_gps_acc = 'FB_ELEC_GPS_ACC'
        fb_elec_gps_nav = 'FB_ELEC_GPS_NAV'
        fb_elec_gps_trk = 'FB_ELEC_GPS_TRK'
        fb_elec_marine = 'FB_ELEC_MARINE'
        fb_elec_network = 'FB_ELEC_NETWORK'
        fb_elec_part = 'FB_ELEC_PART'
        fb_elec_print = 'FB_ELEC_PRINT'
        fb_elec_radar = 'FB_ELEC_RADAR'
        fb_elec_sftwr = 'FB_ELEC_SFTWR'
        fb_elec_speed_rdr = 'FB_ELEC_SPEED_RDR'
        fb_elec_television = 'FB_ELEC_TELEVISION'
        fb_elec_toll = 'FB_ELEC_TOLL'
        fb_elec_video = 'FB_ELEC_VIDEO'
        fb_elec_vid_gm_acc = 'FB_ELEC_VID_GM_ACC'
        fb_elec_vid_gm_cnsl = 'FB_ELEC_VID_GM_CNSL'
        fb_food = 'FB_FOOD'
        fb_furn = 'FB_FURN'
        fb_furn_baby = 'FB_FURN_BABY'
        fb_furn_bench = 'FB_FURN_BENCH'
        fb_furn_cart = 'FB_FURN_CART'
        fb_furn_chair = 'FB_FURN_CHAIR'
        fb_furn_chair_acc = 'FB_FURN_CHAIR_ACC'
        fb_furn_divide = 'FB_FURN_DIVIDE'
        fb_furn_divide_acc = 'FB_FURN_DIVIDE_ACC'
        fb_furn_ent_ctr = 'FB_FURN_ENT_CTR'
        fb_furn_futn = 'FB_FURN_FUTN'
        fb_furn_futn_pad = 'FB_FURN_FUTN_PAD'
        fb_furn_office = 'FB_FURN_OFFICE'
        fb_furn_office_acc = 'FB_FURN_OFFICE_ACC'
        fb_furn_otto = 'FB_FURN_OTTO'
        fb_furn_outdoor = 'FB_FURN_OUTDOOR'
        fb_furn_outdoor_acc = 'FB_FURN_OUTDOOR_ACC'
        fb_furn_sets = 'FB_FURN_SETS'
        fb_furn_shelve_acc = 'FB_FURN_SHELVE_ACC'
        fb_furn_shlf = 'FB_FURN_SHLF'
        fb_furn_sofa = 'FB_FURN_SOFA'
        fb_furn_sofa_acc = 'FB_FURN_SOFA_ACC'
        fb_furn_storage = 'FB_FURN_STORAGE'
        fb_furn_tabl = 'FB_FURN_TABL'
        fb_furn_tabl_acc = 'FB_FURN_TABL_ACC'
        fb_generic_taxable = 'FB_GENERIC_TAXABLE'
        fb_hlth = 'FB_HLTH'
        fb_hlth_hlth = 'FB_HLTH_HLTH'
        fb_hlth_jwl_cr = 'FB_HLTH_JWL_CR'
        fb_hlth_lilp_blm = 'FB_HLTH_LILP_BLM'
        fb_hlth_ltn_spf = 'FB_HLTH_LTN_SPF'
        fb_hlth_prsl_cr = 'FB_HLTH_PRSL_CR'
        fb_hlth_skn_cr = 'FB_HLTH_SKN_CR'
        fb_hmgn = 'FB_HMGN'
        fb_hmgn_bath = 'FB_HMGN_BATH'
        fb_hmgn_dcor = 'FB_HMGN_DCOR'
        fb_hmgn_emgy = 'FB_HMGN_EMGY'
        fb_hmgn_fplc = 'FB_HMGN_FPLC'
        fb_hmgn_fplc_acc = 'FB_HMGN_FPLC_ACC'
        fb_hmgn_gs_sft = 'FB_HMGN_GS_SFT'
        fb_hmgn_hs_acc = 'FB_HMGN_HS_ACC'
        fb_hmgn_hs_app = 'FB_HMGN_HS_APP'
        fb_hmgn_hs_spl = 'FB_HMGN_HS_SPL'
        fb_hmgn_ktcn = 'FB_HMGN_KTCN'
        fb_hmgn_lawn = 'FB_HMGN_LAWN'
        fb_hmgn_lght = 'FB_HMGN_LGHT'
        fb_hmgn_linn = 'FB_HMGN_LINN'
        fb_hmgn_lt_acc = 'FB_HMGN_LT_ACC'
        fb_hmgn_otdr = 'FB_HMGN_OTDR'
        fb_hmgn_pool = 'FB_HMGN_POOL'
        fb_hmgn_scty = 'FB_HMGN_SCTY'
        fb_hmgn_smk_acc = 'FB_HMGN_SMK_ACC'
        fb_hmgn_umbr = 'FB_HMGN_UMBR'
        fb_hmgn_umbr_acc = 'FB_HMGN_UMBR_ACC'
        fb_mdia = 'FB_MDIA'
        fb_mdia_book = 'FB_MDIA_BOOK'
        fb_mdia_dvds = 'FB_MDIA_DVDS'
        fb_mdia_mag = 'FB_MDIA_MAG'
        fb_mdia_manl = 'FB_MDIA_MANL'
        fb_mdia_musc = 'FB_MDIA_MUSC'
        fb_mdia_prj_pln = 'FB_MDIA_PRJ_PLN'
        fb_mdia_sht_mus = 'FB_MDIA_SHT_MUS'
        fb_offc = 'FB_OFFC'
        fb_offc_bkac = 'FB_OFFC_BKAC'
        fb_offc_crts = 'FB_OFFC_CRTS'
        fb_offc_dskp = 'FB_OFFC_DSKP'
        fb_offc_eqip = 'FB_OFFC_EQIP'
        fb_offc_flng = 'FB_OFFC_FLNG'
        fb_offc_gnrl = 'FB_OFFC_GNRL'
        fb_offc_instm = 'FB_OFFC_INSTM'
        fb_offc_lp_dsk = 'FB_OFFC_LP_DSK'
        fb_offc_mats = 'FB_OFFC_MATS'
        fb_offc_nm_plt = 'FB_OFFC_NM_PLT'
        fb_offc_ppr_hndl = 'FB_OFFC_PPR_HNDL'
        fb_offc_prsnt_spl = 'FB_OFFC_PRSNT_SPL'
        fb_offc_sealr = 'FB_OFFC_SEALR'
        fb_offc_ship_spl = 'FB_OFFC_SHIP_SPL'
        fb_rlgn = 'FB_RLGN'
        fb_rlgn_cmny = 'FB_RLGN_CMNY'
        fb_rlgn_item = 'FB_RLGN_ITEM'
        fb_rlgn_wedd = 'FB_RLGN_WEDD'
        fb_sftwr = 'FB_SFTWR'
        fb_sfwr_cmptr = 'FB_SFWR_CMPTR'
        fb_sfwr_dgtl_gd = 'FB_SFWR_DGTL_GD'
        fb_sfwr_game = 'FB_SFWR_GAME'
        fb_shipping = 'FB_SHIPPING'
        fb_spor = 'FB_SPOR'
        fb_sport_athl = 'FB_SPORT_ATHL'
        fb_sport_athl_clth = 'FB_SPORT_ATHL_CLTH'
        fb_sport_athl_shoe = 'FB_SPORT_ATHL_SHOE'
        fb_sport_athl_sprt = 'FB_SPORT_ATHL_SPRT'
        fb_sport_exrcs = 'FB_SPORT_EXRCS'
        fb_sport_indr_gm = 'FB_SPORT_INDR_GM'
        fb_sport_otdr_gm = 'FB_SPORT_OTDR_GM'
        fb_toys = 'FB_TOYS'
        fb_toys_eqip = 'FB_TOYS_EQIP'
        fb_toys_game = 'FB_TOYS_GAME'
        fb_toys_pzzl = 'FB_TOYS_PZZL'
        fb_toys_tmrs = 'FB_TOYS_TMRS'
        fb_toys_toys = 'FB_TOYS_TOYS'
        fb_vehi = 'FB_VEHI'
        fb_vehi_part = 'FB_VEHI_PART'

    class ErrorPriority:
        high = 'HIGH'
        low = 'LOW'
        medium = 'MEDIUM'

    class ErrorType:
        address_blocklisted_in_market = 'ADDRESS_BLOCKLISTED_IN_MARKET'
        aggregated_localization_issues = 'AGGREGATED_LOCALIZATION_ISSUES'
        app_has_no_aem_setup = 'APP_HAS_NO_AEM_SETUP'
        ar_deleted_due_to_update = 'AR_DELETED_DUE_TO_UPDATE'
        ar_policy_violated = 'AR_POLICY_VIOLATED'
        available = 'AVAILABLE'
        bad_quality_image = 'BAD_QUALITY_IMAGE'
        big_catalog_with_all_items_in_stock = 'BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK'
        biz_msg_ai_agent_disabled_by_user = 'BIZ_MSG_AI_AGENT_DISABLED_BY_USER'
        biz_msg_gen_ai_policy_violated = 'BIZ_MSG_GEN_AI_POLICY_VIOLATED'
        cannot_edit_subscription_products = 'CANNOT_EDIT_SUBSCRIPTION_PRODUCTS'
        catalog_not_connected_to_event_source = 'CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE'
        checkout_disabled_by_user = 'CHECKOUT_DISABLED_BY_USER'
        commerce_account_legal_address_invalid = 'COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID'
        commerce_account_not_legally_compliant = 'COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT'
        crawled_availability_mismatch = 'CRAWLED_AVAILABILITY_MISMATCH'
        da_disabled_by_user = 'DA_DISABLED_BY_USER'
        da_policy_unfit_for_audience = 'DA_POLICY_UNFIT_FOR_AUDIENCE'
        da_policy_violation = 'DA_POLICY_VIOLATION'
        deleted_item = 'DELETED_ITEM'
        digital_goods_not_available_for_checkout = 'DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT'
        duplicate_images = 'DUPLICATE_IMAGES'
        duplicate_title_and_description = 'DUPLICATE_TITLE_AND_DESCRIPTION'
        empty_availability = 'EMPTY_AVAILABILITY'
        empty_condition = 'EMPTY_CONDITION'
        empty_description = 'EMPTY_DESCRIPTION'
        empty_image_url = 'EMPTY_IMAGE_URL'
        empty_price = 'EMPTY_PRICE'
        empty_product_url = 'EMPTY_PRODUCT_URL'
        empty_seller_description = 'EMPTY_SELLER_DESCRIPTION'
        empty_title = 'EMPTY_TITLE'
        external_merchant_id_mismatch = 'EXTERNAL_MERCHANT_ID_MISMATCH'
        generic_invalid_field = 'GENERIC_INVALID_FIELD'
        groups_disabled_by_user = 'GROUPS_DISABLED_BY_USER'
        hidden_until_product_launch = 'HIDDEN_UNTIL_PRODUCT_LAUNCH'
        illegal_product_category = 'ILLEGAL_PRODUCT_CATEGORY'
        image_fetch_failed = 'IMAGE_FETCH_FAILED'
        image_fetch_failed_bad_gateway = 'IMAGE_FETCH_FAILED_BAD_GATEWAY'
        image_fetch_failed_file_size_exceeded = 'IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED'
        image_fetch_failed_forbidden = 'IMAGE_FETCH_FAILED_FORBIDDEN'
        image_fetch_failed_link_broken = 'IMAGE_FETCH_FAILED_LINK_BROKEN'
        image_fetch_failed_timed_out = 'IMAGE_FETCH_FAILED_TIMED_OUT'
        image_resolution_low = 'IMAGE_RESOLUTION_LOW'
        inactive_shopify_product = 'INACTIVE_SHOPIFY_PRODUCT'
        invalid_commerce_tax_category = 'INVALID_COMMERCE_TAX_CATEGORY'
        invalid_consolidated_locality_information = 'INVALID_CONSOLIDATED_LOCALITY_INFORMATION'
        invalid_content_id = 'INVALID_CONTENT_ID'
        invalid_dealer_communication_parameters = 'INVALID_DEALER_COMMUNICATION_PARAMETERS'
        invalid_dma_codes = 'INVALID_DMA_CODES'
        invalid_fb_page_id = 'INVALID_FB_PAGE_ID'
        invalid_images = 'INVALID_IMAGES'
        invalid_monetizer_return_policy = 'INVALID_MONETIZER_RETURN_POLICY'
        invalid_offer_disclaimer_url = 'INVALID_OFFER_DISCLAIMER_URL'
        invalid_offer_end_date = 'INVALID_OFFER_END_DATE'
        invalid_pre_order_params = 'INVALID_PRE_ORDER_PARAMS'
        invalid_range_for_area_size = 'INVALID_RANGE_FOR_AREA_SIZE'
        invalid_range_for_built_up_area_size = 'INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE'
        invalid_range_for_num_of_baths = 'INVALID_RANGE_FOR_NUM_OF_BATHS'
        invalid_range_for_num_of_beds = 'INVALID_RANGE_FOR_NUM_OF_BEDS'
        invalid_range_for_num_of_rooms = 'INVALID_RANGE_FOR_NUM_OF_ROOMS'
        invalid_range_for_parking_spaces = 'INVALID_RANGE_FOR_PARKING_SPACES'
        invalid_shelter_page_id = 'INVALID_SHELTER_PAGE_ID'
        invalid_shipping_profile_params = 'INVALID_SHIPPING_PROFILE_PARAMS'
        invalid_subscription_disable_params = 'INVALID_SUBSCRIPTION_DISABLE_PARAMS'
        invalid_subscription_enable_params = 'INVALID_SUBSCRIPTION_ENABLE_PARAMS'
        invalid_subscription_params = 'INVALID_SUBSCRIPTION_PARAMS'
        invalid_tax_extension_state = 'INVALID_TAX_EXTENSION_STATE'
        invalid_vehicle_state = 'INVALID_VEHICLE_STATE'
        invalid_virtual_tour_url_domain = 'INVALID_VIRTUAL_TOUR_URL_DOMAIN'
        inventory_zero_availability_in_stock = 'INVENTORY_ZERO_AVAILABILITY_IN_STOCK'
        in_another_product_launch = 'IN_ANOTHER_PRODUCT_LAUNCH'
        item_group_not_specified = 'ITEM_GROUP_NOT_SPECIFIED'
        item_not_shippable_for_sca_shop = 'ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP'
        item_override_empty_availability = 'ITEM_OVERRIDE_EMPTY_AVAILABILITY'
        item_override_empty_price = 'ITEM_OVERRIDE_EMPTY_PRICE'
        item_override_not_visible = 'ITEM_OVERRIDE_NOT_VISIBLE'
        item_price_not_positive = 'ITEM_PRICE_NOT_POSITIVE'
        item_stale_out_of_stock = 'ITEM_STALE_OUT_OF_STOCK'
        marketplace_disabled_by_user = 'MARKETPLACE_DISABLED_BY_USER'
        marketplace_partner_auction_no_bid_close_time = 'MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME'
        marketplace_partner_currency_not_valid = 'MARKETPLACE_PARTNER_CURRENCY_NOT_VALID'
        marketplace_partner_listing_country_not_match_catalog = 'MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG'
        marketplace_partner_listing_limit_exceeded = 'MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED'
        marketplace_partner_missing_latlong = 'MARKETPLACE_PARTNER_MISSING_LATLONG'
        marketplace_partner_missing_shipping_cost = 'MARKETPLACE_PARTNER_MISSING_SHIPPING_COST'
        marketplace_partner_not_local_item = 'MARKETPLACE_PARTNER_NOT_LOCAL_ITEM'
        marketplace_partner_not_shipped_item = 'MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM'
        marketplace_partner_policy_violation = 'MARKETPLACE_PARTNER_POLICY_VIOLATION'
        marketplace_partner_rule_listing_limit_exceeded = 'MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED'
        marketplace_partner_seller_banned = 'MARKETPLACE_PARTNER_SELLER_BANNED'
        marketplace_partner_seller_not_valid = 'MARKETPLACE_PARTNER_SELLER_NOT_VALID'
        mini_shops_disabled_by_user = 'MINI_SHOPS_DISABLED_BY_USER'
        missing_checkout = 'MISSING_CHECKOUT'
        missing_checkout_currency = 'MISSING_CHECKOUT_CURRENCY'
        missing_color = 'MISSING_COLOR'
        missing_country_override_in_shipping_profile = 'MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE'
        missing_event = 'MISSING_EVENT'
        missing_india_compliance_fields = 'MISSING_INDIA_COMPLIANCE_FIELDS'
        missing_shipping_profile = 'MISSING_SHIPPING_PROFILE'
        missing_size = 'MISSING_SIZE'
        missing_tax_category = 'MISSING_TAX_CATEGORY'
        negative_community_feedback = 'NEGATIVE_COMMUNITY_FEEDBACK'
        negative_price = 'NEGATIVE_PRICE'
        not_enough_images = 'NOT_ENOUGH_IMAGES'
        not_enough_unique_products = 'NOT_ENOUGH_UNIQUE_PRODUCTS'
        no_content_id = 'NO_CONTENT_ID'
        overlay_disclaimer_exceeded_max_length = 'OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH'
        part_of_product_launch = 'PART_OF_PRODUCT_LAUNCH'
        passing_multiple_content_ids = 'PASSING_MULTIPLE_CONTENT_IDS'
        product_dominant_currency_mismatch = 'PRODUCT_DOMINANT_CURRENCY_MISMATCH'
        product_expired = 'PRODUCT_EXPIRED'
        product_item_hidden_from_all_shops = 'PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS'
        product_item_invalid_partner_tokens = 'PRODUCT_ITEM_INVALID_PARTNER_TOKENS'
        product_item_not_included_in_any_shop = 'PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP'
        product_item_not_visible = 'PRODUCT_ITEM_NOT_VISIBLE'
        product_not_approved = 'PRODUCT_NOT_APPROVED'
        product_not_dominant_currency = 'PRODUCT_NOT_DOMINANT_CURRENCY'
        product_out_of_stock = 'PRODUCT_OUT_OF_STOCK'
        product_url_equals_domain = 'PRODUCT_URL_EQUALS_DOMAIN'
        property_price_currency_not_supported = 'PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED'
        property_price_too_high = 'PROPERTY_PRICE_TOO_HIGH'
        property_price_too_low = 'PROPERTY_PRICE_TOO_LOW'
        property_unit_price_currency_mismatch_item_price_currency = 'PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY'
        property_value_contains_html_tags = 'PROPERTY_VALUE_CONTAINS_HTML_TAGS'
        property_value_description_contains_off_platform_link = 'PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK'
        property_value_format = 'PROPERTY_VALUE_FORMAT'
        property_value_missing = 'PROPERTY_VALUE_MISSING'
        property_value_missing_warning = 'PROPERTY_VALUE_MISSING_WARNING'
        property_value_non_positive = 'PROPERTY_VALUE_NON_POSITIVE'
        property_value_string_exceeds_length = 'PROPERTY_VALUE_STRING_EXCEEDS_LENGTH'
        property_value_string_too_short = 'PROPERTY_VALUE_STRING_TOO_SHORT'
        property_value_uppercase = 'PROPERTY_VALUE_UPPERCASE'
        property_value_uppercase_warning = 'PROPERTY_VALUE_UPPERCASE_WARNING'
        purchase_rate_below_addtocart = 'PURCHASE_RATE_BELOW_ADDTOCART'
        purchase_rate_below_viewcontent = 'PURCHASE_RATE_BELOW_VIEWCONTENT'
        quality_duplicated_description = 'QUALITY_DUPLICATED_DESCRIPTION'
        quality_item_link_broken = 'QUALITY_ITEM_LINK_BROKEN'
        quality_item_link_redirecting = 'QUALITY_ITEM_LINK_REDIRECTING'
        retailer_id_not_provided = 'RETAILER_ID_NOT_PROVIDED'
        shopify_invalid_retailer_id = 'SHOPIFY_INVALID_RETAILER_ID'
        shopify_item_missing_shipping_profile = 'SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE'
        shops_policy_violation = 'SHOPS_POLICY_VIOLATION'
        subscription_info_not_enabled_for_feed = 'SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED'
        tax_category_not_supported_in_uk = 'TAX_CATEGORY_NOT_SUPPORTED_IN_UK'
        unique_product_identifier_missing = 'UNIQUE_PRODUCT_IDENTIFIER_MISSING'
        unmatched_events = 'UNMATCHED_EVENTS'
        unsupported_product_category = 'UNSUPPORTED_PRODUCT_CATEGORY'
        variant_attribute_issue = 'VARIANT_ATTRIBUTE_ISSUE'
        video_fetch_failed = 'VIDEO_FETCH_FAILED'
        video_fetch_failed_bad_gateway = 'VIDEO_FETCH_FAILED_BAD_GATEWAY'
        video_fetch_failed_file_size_exceeded = 'VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED'
        video_fetch_failed_forbidden = 'VIDEO_FETCH_FAILED_FORBIDDEN'
        video_fetch_failed_link_broken = 'VIDEO_FETCH_FAILED_LINK_BROKEN'
        video_fetch_failed_timed_out = 'VIDEO_FETCH_FAILED_TIMED_OUT'
        video_not_downloadable = 'VIDEO_NOT_DOWNLOADABLE'
        whatsapp_disabled_by_user = 'WHATSAPP_DISABLED_BY_USER'
        whatsapp_marketing_message_disabled_by_user = 'WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER'
        whatsapp_marketing_message_policy_violation = 'WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION'
        whatsapp_policy_violation = 'WHATSAPP_POLICY_VIOLATION'

    class MarkedForProductLaunch:
        value_default = 'default'
        marked = 'marked'
        not_marked = 'not_marked'

    class OriginCountry:
        ad = 'AD'
        ae = 'AE'
        af = 'AF'
        ag = 'AG'
        ai = 'AI'
        al = 'AL'
        am = 'AM'
        an = 'AN'
        ao = 'AO'
        aq = 'AQ'
        ar = 'AR'
        value_as = 'AS'
        at = 'AT'
        au = 'AU'
        aw = 'AW'
        ax = 'AX'
        az = 'AZ'
        ba = 'BA'
        bb = 'BB'
        bd = 'BD'
        be = 'BE'
        bf = 'BF'
        bg = 'BG'
        bh = 'BH'
        bi = 'BI'
        bj = 'BJ'
        bl = 'BL'
        bm = 'BM'
        bn = 'BN'
        bo = 'BO'
        bq = 'BQ'
        br = 'BR'
        bs = 'BS'
        bt = 'BT'
        bv = 'BV'
        bw = 'BW'
        by = 'BY'
        bz = 'BZ'
        ca = 'CA'
        cc = 'CC'
        cd = 'CD'
        cf = 'CF'
        cg = 'CG'
        ch = 'CH'
        ci = 'CI'
        ck = 'CK'
        cl = 'CL'
        cm = 'CM'
        cn = 'CN'
        co = 'CO'
        cr = 'CR'
        cu = 'CU'
        cv = 'CV'
        cw = 'CW'
        cx = 'CX'
        cy = 'CY'
        cz = 'CZ'
        de = 'DE'
        dj = 'DJ'
        dk = 'DK'
        dm = 'DM'
        do = 'DO'
        dz = 'DZ'
        ec = 'EC'
        ee = 'EE'
        eg = 'EG'
        eh = 'EH'
        er = 'ER'
        es = 'ES'
        et = 'ET'
        fi = 'FI'
        fj = 'FJ'
        fk = 'FK'
        fm = 'FM'
        fo = 'FO'
        fr = 'FR'
        ga = 'GA'
        gb = 'GB'
        gd = 'GD'
        ge = 'GE'
        gf = 'GF'
        gg = 'GG'
        gh = 'GH'
        gi = 'GI'
        gl = 'GL'
        gm = 'GM'
        gn = 'GN'
        gp = 'GP'
        gq = 'GQ'
        gr = 'GR'
        gs = 'GS'
        gt = 'GT'
        gu = 'GU'
        gw = 'GW'
        gy = 'GY'
        hk = 'HK'
        hm = 'HM'
        hn = 'HN'
        hr = 'HR'
        ht = 'HT'
        hu = 'HU'
        id = 'ID'
        ie = 'IE'
        il = 'IL'
        im = 'IM'
        value_in = 'IN'
        io = 'IO'
        iq = 'IQ'
        ir = 'IR'
        value_is = 'IS'
        it = 'IT'
        je = 'JE'
        jm = 'JM'
        jo = 'JO'
        jp = 'JP'
        ke = 'KE'
        kg = 'KG'
        kh = 'KH'
        ki = 'KI'
        km = 'KM'
        kn = 'KN'
        kp = 'KP'
        kr = 'KR'
        kw = 'KW'
        ky = 'KY'
        kz = 'KZ'
        la = 'LA'
        lb = 'LB'
        lc = 'LC'
        li = 'LI'
        lk = 'LK'
        lr = 'LR'
        ls = 'LS'
        lt = 'LT'
        lu = 'LU'
        lv = 'LV'
        ly = 'LY'
        ma = 'MA'
        mc = 'MC'
        md = 'MD'
        me = 'ME'
        mf = 'MF'
        mg = 'MG'
        mh = 'MH'
        mk = 'MK'
        ml = 'ML'
        mm = 'MM'
        mn = 'MN'
        mo = 'MO'
        mp = 'MP'
        mq = 'MQ'
        mr = 'MR'
        ms = 'MS'
        mt = 'MT'
        mu = 'MU'
        mv = 'MV'
        mw = 'MW'
        mx = 'MX'
        my = 'MY'
        mz = 'MZ'
        na = 'NA'
        nc = 'NC'
        ne = 'NE'
        nf = 'NF'
        ng = 'NG'
        ni = 'NI'
        nl = 'NL'
        no = 'NO'
        np = 'NP'
        nr = 'NR'
        nu = 'NU'
        nz = 'NZ'
        om = 'OM'
        pa = 'PA'
        pe = 'PE'
        pf = 'PF'
        pg = 'PG'
        ph = 'PH'
        pk = 'PK'
        pl = 'PL'
        pm = 'PM'
        pn = 'PN'
        pr = 'PR'
        ps = 'PS'
        pt = 'PT'
        pw = 'PW'
        py = 'PY'
        qa = 'QA'
        re = 'RE'
        ro = 'RO'
        rs = 'RS'
        ru = 'RU'
        rw = 'RW'
        sa = 'SA'
        sb = 'SB'
        sc = 'SC'
        sd = 'SD'
        se = 'SE'
        sg = 'SG'
        sh = 'SH'
        si = 'SI'
        sj = 'SJ'
        sk = 'SK'
        sl = 'SL'
        sm = 'SM'
        sn = 'SN'
        so = 'SO'
        sr = 'SR'
        ss = 'SS'
        st = 'ST'
        sv = 'SV'
        sx = 'SX'
        sy = 'SY'
        sz = 'SZ'
        tc = 'TC'
        td = 'TD'
        tf = 'TF'
        tg = 'TG'
        th = 'TH'
        tj = 'TJ'
        tk = 'TK'
        tl = 'TL'
        tm = 'TM'
        tn = 'TN'
        to = 'TO'
        tr = 'TR'
        tt = 'TT'
        tv = 'TV'
        tw = 'TW'
        tz = 'TZ'
        ua = 'UA'
        ug = 'UG'
        um = 'UM'
        us = 'US'
        uy = 'UY'
        uz = 'UZ'
        va = 'VA'
        vc = 'VC'
        ve = 'VE'
        vg = 'VG'
        vi = 'VI'
        vn = 'VN'
        vu = 'VU'
        wf = 'WF'
        ws = 'WS'
        xk = 'XK'
        ye = 'YE'
        yt = 'YT'
        za = 'ZA'
        zm = 'ZM'
        zw = 'ZW'

    class WaComplianceCategory:
        country_origin_exempt = 'COUNTRY_ORIGIN_EXEMPT'
        value_default = 'DEFAULT'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'products'

    # @deprecated api_create is being deprecated
    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_product(fields, params, batch, success, failure, pending)

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'catalog_id': 'string',
            'image_height': 'unsigned int',
            'image_width': 'unsigned int',
            'override_country': 'string',
            'override_language': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'additional_image_urls': 'list<string>',
            'additional_variant_attributes': 'map',
            'age_group': 'age_group_enum',
            'android_app_name': 'string',
            'android_class': 'string',
            'android_package': 'string',
            'android_url': 'string',
            'availability': 'availability_enum',
            'brand': 'string',
            'category': 'string',
            'category_specific_fields': 'map',
            'checkout_url': 'string',
            'color': 'string',
            'commerce_tax_category': 'commerce_tax_category_enum',
            'condition': 'condition_enum',
            'currency': 'string',
            'custom_data': 'map',
            'custom_label_0': 'string',
            'custom_label_1': 'string',
            'custom_label_2': 'string',
            'custom_label_3': 'string',
            'custom_label_4': 'string',
            'custom_number_0': 'unsigned int',
            'custom_number_1': 'unsigned int',
            'custom_number_2': 'unsigned int',
            'custom_number_3': 'unsigned int',
            'custom_number_4': 'unsigned int',
            'description': 'string',
            'expiration_date': 'string',
            'fb_product_category': 'string',
            'gender': 'gender_enum',
            'gtin': 'string',
            'image_url': 'string',
            'importer_address': 'map',
            'importer_name': 'string',
            'inventory': 'unsigned int',
            'ios_app_name': 'string',
            'ios_app_store_id': 'unsigned int',
            'ios_url': 'string',
            'ipad_app_name': 'string',
            'ipad_app_store_id': 'unsigned int',
            'ipad_url': 'string',
            'iphone_app_name': 'string',
            'iphone_app_store_id': 'unsigned int',
            'iphone_url': 'string',
            'launch_date': 'string',
            'manufacturer_info': 'string',
            'manufacturer_part_number': 'string',
            'marked_for_product_launch': 'marked_for_product_launch_enum',
            'material': 'string',
            'mobile_link': 'string',
            'name': 'string',
            'ordering_index': 'unsigned int',
            'origin_country': 'origin_country_enum',
            'pattern': 'string',
            'price': 'unsigned int',
            'product_priority_0': 'float',
            'product_priority_1': 'float',
            'product_priority_2': 'float',
            'product_priority_3': 'float',
            'product_priority_4': 'float',
            'product_type': 'string',
            'quantity_to_sell_on_facebook': 'unsigned int',
            'retailer_id': 'string',
            'return_policy_days': 'unsigned int',
            'sale_price': 'unsigned int',
            'sale_price_end_date': 'datetime',
            'sale_price_start_date': 'datetime',
            'short_description': 'string',
            'size': 'string',
            'start_date': 'string',
            'url': 'string',
            'visibility': 'visibility_enum',
            'wa_compliance_category': 'wa_compliance_category_enum',
            'windows_phone_app_id': 'string',
            'windows_phone_app_name': 'string',
            'windows_phone_url': 'string',
        }
        enums = {
            'age_group_enum': ProductItem.AgeGroup.__dict__.values(),
            'availability_enum': ProductItem.Availability.__dict__.values(),
            'commerce_tax_category_enum': ProductItem.CommerceTaxCategory.__dict__.values(),
            'condition_enum': ProductItem.Condition.__dict__.values(),
            'gender_enum': ProductItem.Gender.__dict__.values(),
            'marked_for_product_launch_enum': ProductItem.MarkedForProductLaunch.__dict__.values(),
            'origin_country_enum': ProductItem.OriginCountry.__dict__.values(),
            'visibility_enum': ProductItem.Visibility.__dict__.values(),
            'wa_compliance_category_enum': ProductItem.WaComplianceCategory.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_channels_to_integrity_status(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.catalogitemchannelstointegritystatus import CatalogItemChannelsToIntegrityStatus
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/channels_to_integrity_status',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CatalogItemChannelsToIntegrityStatus,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CatalogItemChannelsToIntegrityStatus, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_override_details(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.overridedetails import OverrideDetails
        param_types = {
            'keys': 'list<string>',
            'type': 'type_enum',
        }
        enums = {
            'type_enum': OverrideDetails.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/override_details',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OverrideDetails,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OverrideDetails, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_product_sets(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.productset import ProductSet
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductSet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_videos_metadata(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.dynamicvideometadata import DynamicVideoMetadata
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/videos_metadata',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DynamicVideoMetadata,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DynamicVideoMetadata, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'additional_image_cdn_urls': 'list<list<map<string, string>>>',
        'additional_image_urls': 'list<string>',
        'additional_variant_attributes': 'list<map<string, string>>',
        'age_group': 'AgeGroup',
        'applinks': 'CatalogItemAppLinks',
        'availability': 'Availability',
        'brand': 'string',
        'bundle_items': 'list<string>',
        'bundle_retailer_ids': 'list<string>',
        'capability_to_review_status': 'list<map<string, ProductItem_capability_to_review_status>>',
        'category': 'string',
        'category_specific_fields': 'CatalogSubVerticalList',
        'color': 'string',
        'commerce_insights': 'ProductItemCommerceInsights',
        'condition': 'Condition',
        'currency': 'string',
        'custom_data': 'list<map<string, string>>',
        'custom_label_0': 'string',
        'custom_label_1': 'string',
        'custom_label_2': 'string',
        'custom_label_3': 'string',
        'custom_label_4': 'string',
        'custom_number_0': 'string',
        'custom_number_1': 'string',
        'custom_number_2': 'string',
        'custom_number_3': 'string',
        'custom_number_4': 'string',
        'description': 'string',
        'errors': 'list<ProductItemError>',
        'expiration_date': 'string',
        'fb_product_category': 'string',
        'gender': 'Gender',
        'generated_background_images': 'list<AIGeneratedProductImage>',
        'generated_background_images_ad_usage': 'bool',
        'gtin': 'string',
        'id': 'string',
        'image_cdn_urls': 'list<map<string, string>>',
        'image_fetch_status': 'ImageFetchStatus',
        'image_url': 'string',
        'images': 'list<string>',
        'importer_address': 'ProductItemImporterAddress',
        'importer_name': 'string',
        'invalidation_errors': 'list<ProductItemInvalidationError>',
        'inventory': 'int',
        'is_bundle_hero': 'bool',
        'manufacturer_info': 'string',
        'manufacturer_part_number': 'string',
        'marked_for_product_launch': 'string',
        'material': 'string',
        'mobile_link': 'string',
        'name': 'string',
        'ordering_index': 'int',
        'origin_country': 'string',
        'parent_product_id': 'string',
        'pattern': 'string',
        'post_conversion_signal_based_enforcement_appeal_eligibility': 'bool',
        'price': 'string',
        'product_catalog': 'ProductCatalog',
        'product_feed': 'ProductFeed',
        'product_group': 'ProductGroup',
        'product_local_info': 'ProductItemLocalInfo',
        'product_relationship': 'string',
        'product_type': 'string',
        'quantity_to_sell_on_facebook': 'int',
        'retailer_id': 'string',
        'retailer_product_group_id': 'string',
        'review_rejection_reasons': 'list<string>',
        'review_status': 'ReviewStatus',
        'sale_price': 'string',
        'sale_price_end_date': 'string',
        'sale_price_start_date': 'string',
        'shipping_weight_unit': 'ShippingWeightUnit',
        'shipping_weight_value': 'float',
        'short_description': 'string',
        'size': 'string',
        'start_date': 'string',
        'tags': 'list<string>',
        'url': 'string',
        'vendor_id': 'string',
        'video_fetch_status': 'VideoFetchStatus',
        'videos': 'list<ProductItemVideoData>',
        'visibility': 'Visibility',
        'wa_compliance_category': 'string',
        'android_app_name': 'string',
        'android_class': 'string',
        'android_package': 'string',
        'android_url': 'string',
        'checkout_url': 'string',
        'commerce_tax_category': 'CommerceTaxCategory',
        'ios_app_name': 'string',
        'ios_app_store_id': 'unsigned int',
        'ios_url': 'string',
        'ipad_app_name': 'string',
        'ipad_app_store_id': 'unsigned int',
        'ipad_url': 'string',
        'iphone_app_name': 'string',
        'iphone_app_store_id': 'unsigned int',
        'iphone_url': 'string',
        'launch_date': 'string',
        'product_priority_0': 'float',
        'product_priority_1': 'float',
        'product_priority_2': 'float',
        'product_priority_3': 'float',
        'product_priority_4': 'float',
        'return_policy_days': 'unsigned int',
        'windows_phone_app_id': 'string',
        'windows_phone_app_name': 'string',
        'windows_phone_url': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AgeGroup'] = ProductItem.AgeGroup.__dict__.values()
        field_enum_info['Availability'] = ProductItem.Availability.__dict__.values()
        field_enum_info['CapabilityToReviewStatus'] = ProductItem.CapabilityToReviewStatus.__dict__.values()
        field_enum_info['Condition'] = ProductItem.Condition.__dict__.values()
        field_enum_info['Gender'] = ProductItem.Gender.__dict__.values()
        field_enum_info['ImageFetchStatus'] = ProductItem.ImageFetchStatus.__dict__.values()
        field_enum_info['ReviewStatus'] = ProductItem.ReviewStatus.__dict__.values()
        field_enum_info['ShippingWeightUnit'] = ProductItem.ShippingWeightUnit.__dict__.values()
        field_enum_info['VideoFetchStatus'] = ProductItem.VideoFetchStatus.__dict__.values()
        field_enum_info['Visibility'] = ProductItem.Visibility.__dict__.values()
        field_enum_info['CommerceTaxCategory'] = ProductItem.CommerceTaxCategory.__dict__.values()
        field_enum_info['ErrorPriority'] = ProductItem.ErrorPriority.__dict__.values()
        field_enum_info['ErrorType'] = ProductItem.ErrorType.__dict__.values()
        field_enum_info['MarkedForProductLaunch'] = ProductItem.MarkedForProductLaunch.__dict__.values()
        field_enum_info['OriginCountry'] = ProductItem.OriginCountry.__dict__.values()
        field_enum_info['WaComplianceCategory'] = ProductItem.WaComplianceCategory.__dict__.values()
        return field_enum_info


