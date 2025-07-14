package com.organization.sage.config;

import java.math.BigDecimal;
import java.util.Map;
import java.util.EnumMap;

import com.organization.sage.model.organisation.ParcelType;
import com.organization.sage.model.organisation.ShipmentType;

public class PricingConfig {
    private Map<ShipmentType, BigDecimal> shipmentTypePrices = new EnumMap<>(ShipmentType.class);
    private Map<ParcelType, BigDecimal> parcelTypePrices = new EnumMap<>(ParcelType.class);

    public PricingConfig() {
    }

    public void updateShipmentTypePrice(ShipmentType type, BigDecimal newPrice) {
        shipmentTypePrices.put(type, newPrice);
    }

    public void updateparcelTypePrice(ParcelType type, BigDecimal newPrice) {
        parcelTypePrices.put(type, newPrice);
    }

    public Map<ShipmentType,BigDecimal> getShipmentTypePrice() {
        return shipmentTypePrices;
    }

    public Map<ParcelType, BigDecimal> getparcelTypePrice() {
        return parcelTypePrices;
    }
}