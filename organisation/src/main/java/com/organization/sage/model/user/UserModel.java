package com.organization.sage.model.user;

import com.fasterxml.jackson.annotation.JsonInclude;
 
import java.util.UUID;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class UserModel {
    private UUID id;
    private String name;
    private String phone;
    private String email;
    private String password;
    private String identity;
    private Role role;
    private Location location;
    private Verification verification;
    private String organizationId;

    public UserModel() {
        this.id = UUID.randomUUID(); // Auto-generate UUID
    }

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getOrganizationId() {
        return organizationId;
    }

    public void setOrganizationId(String organizationId) {
        this.organizationId = organizationId;
    }

    public String getIdentity() {
        return identity;
    }

    public void setIdentity(String identity) {
        this.identity = identity;
    }

    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }

    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }


    public Verification getVerification() {
        return verification;
    }

    public void setVerification(Verification verification) {
        this.verification = verification;
    }

    @Override
    public String toString() {
        return "{ " +
                "id:" + id +
                ", name: '" + name + '\'' +
                ", phone: '" + phone + '\'' +
                ", email: '" + email + '\'' +
                ", password: '" + password + '\'' +
                ", identity: '" + identity + '\'' +
                ", role: " + role +
                ", location: " + location +
                ", verification: " + verification +
                ", organizationId: " + organizationId +
                '}';
    }


}

