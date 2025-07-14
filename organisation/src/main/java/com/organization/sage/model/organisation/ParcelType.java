package com.organization.sage.model.organisation;

import java.math.BigDecimal;

public enum ParcelType {
    Document("Document", null),
    Perishable("Perishable", null),
    Fragile("Fragile", null),
    Normal("Normal", null);

    private final String displayName;
    private final BigDecimal price;

    ParcelType(String displayName, BigDecimal price) {
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
