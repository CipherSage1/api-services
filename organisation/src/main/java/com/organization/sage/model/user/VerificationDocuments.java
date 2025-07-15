package com.organization.sage.model.user;

public class VerificationDocuments {
    private String url;
    private String description;

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


    @Override
    public String toString() {
        return "{ " +
                "url: '" + url + '\'' +
                ", description: '" + description + '\'' +
                '}';
    }

    
}
