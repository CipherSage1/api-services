package com.organization.sage.model.organisation;

import java.util.UUID;

import com.fasterxml.jackson.annotation.JsonProperty;
public class Branch {

    private double longitude;
    private double latitude;
    private String branchName;

    @JsonProperty("id")
    private String branchId;

    public Branch() {
        this.branchId = UUID.randomUUID().toString();
    }

    // Getters and Setters

    public double getLongitude() {
        return longitude;
    }

    public void setLongitude(double longitude) {
        this.longitude = longitude;
    }

    public double getLatitude() {
        return latitude;
    }

    public void setLatitude(double latitude) {
        this.latitude = latitude;
    }

    public String getBranchName() {
        return branchName;
    }

    public void setBranchName(String branchName) {
        this.branchName = branchName;
    }

    public String getBranchId() {
        return branchId;
    }

    public void setBranchId(String branchId) {
        this.branchId = branchId;
    }

    @Override
    public String toString() {
        return "{ " +
                "branchId: '" + branchId + '\'' +
                ", branchName: '" + branchName + '\'' +
                ", latitude: " + latitude +
                ", longitude: " + longitude +
                '}';
    }
}