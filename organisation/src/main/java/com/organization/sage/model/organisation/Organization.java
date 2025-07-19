package com.organization.sage.model.organisation;

import java.util.ArrayList;
import java.util.List; 
import java.util.UUID;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.organization.sage.model.payment.Pricing;

public class Organization {

   @JsonProperty("id")
    private String id;

    private String companyName;

    private List<Branch> branches;

    private String kra;

    private boolean zeroBasedPricing;

    private String clientId;

    private String companyLogo;

    private ArrayList<Pricing> pricing;
 

    public Organization() {
        this.id = UUID.randomUUID().toString();
    }

    // Getters and Setters
    public String getOrganizationId() {
        return id;
    }

    public void setOrganizationId(String organizationId) {
        this.id = organizationId;
    }

    public String getCompanyName() {
        return companyName;
    }

    public void setCompanyLogo(String companyLogo) {
        this.companyLogo = companyLogo;
    }

    public String getCompanyLogo() {
        return companyLogo;
    }

    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }

    public List<Branch> getbranches() {
        return branches;
    }

    public void setbranches(List<Branch> branches) {
        this.branches = branches;
    }

    public String getKra() {
        return kra;
    }

    public void setKra(String kra) {
        this.kra = kra;
    }

    public boolean isZeroBasedPricing() {
        return zeroBasedPricing;
    }

    public void setZeroBasedPricing(boolean zeroBasedPricing) {
        this.zeroBasedPricing = zeroBasedPricing;
    }

    public String getClientId() {
        return clientId;
    }

    public void setClientId(String clientId) {
        this.clientId = clientId;
    }

    public void setPricing(ArrayList<Pricing> pricing) {
        this.pricing = pricing;
    }

    public ArrayList<Pricing> getPricing() {
        return pricing;
    }

    @Override
    public String toString() {
        return "Organization { " +
                "organizationId: '" + id + '\'' +
                ", companyName: '" + companyName + '\'' +
                ", companyLogo: '" + companyLogo + '\'' +
                ", branches: " + branches +
                ", kra: '" + kra + '\'' +
                ", zeroBasedPricing: " + zeroBasedPricing +
                ", clientId: '" + clientId + '\'' +
                ", pricing: " + pricing +
                '}';
    }
}
