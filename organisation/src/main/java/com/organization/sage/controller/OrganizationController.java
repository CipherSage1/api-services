package com.organization.sage.controller;

import java.util.List;
import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.organization.sage.model.ApiResponse;
import com.organization.sage.model.LogType;
import com.organization.sage.model.organisation.Branch;
import com.organization.sage.model.organisation.BranchRequest;
import com.organization.sage.model.organisation.Organization;
import com.organization.sage.model.organisation.PricingRequest;
import com.organization.sage.service.organization.OrganizationService;
import com.organization.sage.utility.Logger;

@RestController
@RequestMapping("/api/internal/organizations")
public class OrganizationController {

    private final OrganizationService organizationService;

    public OrganizationController(OrganizationService organizationService) {
        this.organizationService = organizationService;
    }

    @PostMapping
    public ResponseEntity<ApiResponse<Organization>> createOrganization(@RequestBody Organization org) {
        return ResponseEntity.ok(organizationService.createOrganization(org));
    }

    @PostMapping("/pricing")
    public ResponseEntity<ApiResponse<Organization>> createPricing(@RequestBody PricingRequest pricing) {
        return ResponseEntity.ok(organizationService.createPricing(pricing));
    }

    @GetMapping
    public ResponseEntity<ApiResponse<List<Organization>>> getAllOrganizations() {
        return ResponseEntity.ok(organizationService.getAllOrganizations());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<Organization>> getOrganizationById(@PathVariable String id) {
        return ResponseEntity.ok(organizationService.getOrganizationById(id));
    }

    @PatchMapping("/{id}")
    public ResponseEntity<Void> updateOrganizationPartially(@PathVariable String id,
            @RequestBody Map<String, Object> updates) {
        organizationService.updateOrganizationPartially(id, updates);
        return ResponseEntity.noContent().build();
    }
    

    @PostMapping("/branch")
    public ResponseEntity<ApiResponse<Organization>> updateOrganizationBranch(@RequestBody BranchRequest request) {
        Logger.print("BranchRequest: "+request.toString(), LogType.ERROR);
        return ResponseEntity.ok(organizationService.updateBranches(request));
    }

    @GetMapping("/branch-all")
    public ResponseEntity<ApiResponse<Branch[]>> getAllBranches(String userId) {
        return ResponseEntity.ok(organizationService.getAllBranches(userId));
    }

    @GetMapping("/branch/{userId}/{organizationId}")
    public ResponseEntity<ApiResponse<Branch>> getBranchById(String userId, String organizationId) {
        return ResponseEntity.ok(organizationService.getBranchById(userId, organizationId));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable String id) {
        organizationService.deleteOrganization(id);
        return ResponseEntity.noContent().build();
    }
    
}
