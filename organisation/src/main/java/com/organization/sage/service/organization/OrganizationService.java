package com.organization.sage.service.organization;

import java.util.List;
import java.util.Map;

import com.organization.sage.model.ApiResponse;
import com.organization.sage.model.organisation.Branch;
import com.organization.sage.model.organisation.BranchRequest;
import com.organization.sage.model.organisation.Organization;
import com.organization.sage.model.organisation.PricingRequest; 

public interface OrganizationService {

	public ApiResponse<Organization> createOrganization(Organization org);
	
	public ApiResponse<List<Organization>> getAllOrganizations();
	
	public ApiResponse<Organization> getOrganizationById(String id);
	
	public void updateOrganization(String id, Organization org);
	
	public void deleteOrganization(String id);

	public void updateOrganizationPartially(String id, Map<String, Object> updates);

	public ApiResponse<Organization> createPricing(PricingRequest pricing);

	public ApiResponse<Organization> updateBranches(BranchRequest request);

	public ApiResponse<Branch[]> getAllBranches(String organizationId);

	public ApiResponse<Branch> getBranchById(String branchId, String organizationId);

}