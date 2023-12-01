document.addEventListener('DOMContentLoaded', () => {
    odoo.define('custom_show_default_code.custom_variant_mixin', function (require) {
        "use strict";
        console.log("Test");
//        var VariantMixin = odoo.__DEBUG__.services['website_sale.VariantMixin'];
        var VariantMixin = require('sale.VariantMixin');
        console.log(VariantMixin._onChangeCombination)
        VariantMixin._onChangeCombination = function (ev, $parent, combination) {
                var self = this;
                var $price = $parent.find(".oe_price:first .oe_currency_value");
                var $default_code = $parent.find(".custom_default_sku");
                var $default_price = $parent.find(".oe_default_price:first .oe_currency_value");
                var $optional_price = $parent.find(".oe_optional:first .oe_currency_value");
                $price.text(self._priceToStr(combination.price));
                $default_code.text(combination.default_code);
                $default_price.text(self._priceToStr(combination.list_price));

                console.log(combination.default_code)

                var isCombinationPossible = true;
                if (!_.isUndefined(combination.is_combination_possible)) {
                    isCombinationPossible = combination.is_combination_possible;
                }
                this._toggleDisable($parent, isCombinationPossible);

                if (combination.has_discounted_price) {
                    $default_price
                        .closest('.oe_website_sale')
                        .addClass("discount");
                    $optional_price
                        .closest('.oe_optional')
                        .removeClass('d-none')
                        .css('text-decoration', 'line-through');
                    $default_price.parent().removeClass('d-none');
                } else {
                    $default_price
                        .closest('.oe_website_sale')
                        .removeClass("discount");
                    $optional_price.closest('.oe_optional').addClass('d-none');
                    $default_price.parent().addClass('d-none');
                }

                var rootComponentSelectors = [
                    'tr.js_product',
                    '.oe_website_sale',
                    '.o_product_configurator'
                ];

                // update images only when changing product
                // or when either ids are 'false', meaning dynamic products.
                // Dynamic products don't have images BUT they may have invalid
                // combinations that need to disable the image.
                if (!combination.product_id ||
                    !this.last_product_id ||
                    combination.product_id !== this.last_product_id) {
                    this.last_product_id = combination.product_id;
                    self._updateProductImage(
                        $parent.closest(rootComponentSelectors.join(', ')),
                        combination.display_image,
                        combination.product_id,
                        combination.product_template_id,
                        combination.carousel,
                        isCombinationPossible
                    );
                }

                $parent
                    .find('.product_id')
                    .first()
                    .val(combination.product_id || 0)
                    .trigger('change');

                $parent
                    .find('.product_display_name')
                    .first()
                    .text(combination.display_name);

                $parent
                    .find('.js_raw_price')
                    .first()
                    .text(combination.price)
                    .trigger('change');

                this.handleCustomValues($(ev.target));
            }


        });
});


