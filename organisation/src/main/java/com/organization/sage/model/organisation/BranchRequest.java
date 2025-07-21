package com.organization.sage.model.organisation;

public class BranchRequest {
    private String userId;
    private Branch branch;

    public BranchRequest(Branch branch, String userId) {
        this.branch = branch;
        this.userId = userId;   
    }

    public String getUserId() {
        return userId;
    }

    public Branch getBranch() {
        return branch;
    }

    public void setBranch(Branch branch) {
        this.branch = branch;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }
}
