package com.organization.sage.model.user;

import java.util.List;

public class Verification {
    
    private boolean isPhoneVerified;
    private boolean isEmailVerified;
    private boolean identityVerified;
    private List<VerificationDocuments> documents;


    public boolean isPhoneVerified() {
        return isPhoneVerified;
    }

    public void setPhoneVerified(boolean phoneVerified) {
        isPhoneVerified = phoneVerified;
    }

    public boolean isEmailVerified() {
        return isEmailVerified;
    }

    public void setEmailVerified(boolean emailVerified) {
        isEmailVerified = emailVerified;
    }

    public boolean isIdentityVerified() {
        return identityVerified;
    }

    public void setIdentityVerified(boolean identityVerified) {
        this.identityVerified = identityVerified;
    }

    public List<VerificationDocuments> getDocuments() {
        return documents;
    }

    public void setDocuments(List<VerificationDocuments> documents) {
        this.documents = documents;
    }
    @Override
    public String toString() {
        return "{ " +
                "isPhoneVerified: " + isPhoneVerified +
                ", isEmailVerified: " + isEmailVerified +
                ", identityVerified: " + identityVerified +
                ", documents: " + documents +
                '}';
    }

}
