package com.organization.sage.model.user;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public enum Role {
    ADMIN("System Admin"),
    DEALER("Dealer"),
    AGENT("Agent"),
    USER("User");

    private final String value;

    Role(String value) {
        this.value = value;
    }

    @JsonCreator
    public static Role fromString(String value) {
        for (Role role : Role.values()) {
            if (role.value.equalsIgnoreCase(value)) {
                return role;
            }
        }
        throw new IllegalArgumentException("Unknown role: " + value);
    }

    @JsonValue
    public String toValue() {
        return value;
    }
}
