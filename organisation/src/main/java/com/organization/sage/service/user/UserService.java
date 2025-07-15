package com.organization.sage.service.user;

import com.organization.sage.model.ApiResponse;
import com.organization.sage.model.user.UserModel;

public interface UserService {
    /**
     * Creates a new user.
     *
     * @param user the user to create
     * @return the created user
     */
 
    public ApiResponse<UserModel> updateUserPartially(String id, UserModel updates);

    
}
