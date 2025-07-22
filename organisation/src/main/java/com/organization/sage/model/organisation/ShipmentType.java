package com.organization.sage.model.organisation;

import java.math.BigDecimal;

public enum ShipmentType {
    Standard("Standard", null),
    Express("Express", null),
    Overnight("Overnight", null),
    NextDay("NextDay", null);

    private final String displayName;
    private final BigDecimal price;

    ShipmentType(String displayName, BigDecimal price) {
        this.displayName = displayName;
        this.price = price;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public String getDisplayName() {
        return displayName;
    }

    @Override
    public String toString() {
        return displayName;
    }
}
