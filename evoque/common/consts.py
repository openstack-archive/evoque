# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

RPC_ATTRS = (
    ENGINE_TOPIC,
    ENGINE_DISPATCHER_TOPIC,
    ENGINE_HEALTH_MGR_TOPIC,
    RPC_API_VERSION,
) = (
    'evoque-engine',
    'engine-dispatcher',
    'engine-health_mgr',
    '1.0',
)

RPC_PARAMS = (
    PARAM_SHOW_DELETED, PARAM_SHOW_NESTED, PARAM_LIMIT, PARAM_MARKER,
    PARAM_GLOBAL_PROJECT, PARAM_SHOW_DETAILS,
    PARAM_SORT_DIR, PARAM_SORT_KEYS,
) = (
    'show_deleted', 'show_nested', 'limit', 'marker',
    'global_project', 'show_details',
    'sort_dir', 'sort_keys',
)

ACTION_NAMES = (
    CLUSTER_CREATE, CLUSTER_DELETE, CLUSTER_UPDATE,
    CLUSTER_ADD_NODES, CLUSTER_DEL_NODES, CLUSTER_RESIZE,
    CLUSTER_SCALE_OUT, CLUSTER_SCALE_IN,
    CLUSTER_ATTACH_POLICY, CLUSTER_DETACH_POLICY, CLUSTER_UPDATE_POLICY,

    NODE_CREATE, NODE_DELETE, NODE_UPDATE,
    NODE_JOIN, NODE_LEAVE,

    POLICY_ENABLE, POLICY_DISABLE, POLICY_UPDATE,
) = (
    'CLUSTER_CREATE', 'CLUSTER_DELETE', 'CLUSTER_UPDATE',
    'CLUSTER_ADD_NODES', 'CLUSTER_DEL_NODES', 'CLUSTER_RESIZE',
    'CLUSTER_SCALE_OUT', 'CLUSTER_SCALE_IN',
    'CLUSTER_ATTACH_POLICY', 'CLUSTER_DETACH_POLICY', 'CLUSTER_UPDATE_POLICY',

    'NODE_CREATE', 'NODE_DELETE', 'NODE_UPDATE',
    'NODE_JOIN', 'NODE_LEAVE',

    'POLICY_ENABLE', 'POLICY_DISABLE', 'POLICY_UPDATE',
)

ADJUSTMENT_PARAMS = (
    ADJUSTMENT_TYPE, ADJUSTMENT_NUMBER, ADJUSTMENT_MIN_STEP,
    ADJUSTMENT_MIN_SIZE, ADJUSTMENT_MAX_SIZE, ADJUSTMENT_STRICT,
) = (
    'adjustment_type', 'number', 'min_step',
    'min_size', 'max_size', 'strict',
)

ADJUSTMENT_TYPES = (
    EXACT_CAPACITY, CHANGE_IN_CAPACITY, CHANGE_IN_PERCENTAGE,
) = (
    'EXACT_CAPACITY', 'CHANGE_IN_CAPACITY', 'CHANGE_IN_PERCENTAGE',
)

CLUSTER_ATTRS = (
    CLUSTER_NAME, CLUSTER_PROFILE, CLUSTER_DESIRED_CAPACITY,
    CLUSTER_MIN_SIZE, CLUSTER_MAX_SIZE, CLUSTER_ID, CLUSTER_PARENT,
    CLUSTER_DOMAIN, CLUSTER_PROJECT, CLUSTER_USER,
    CLUSTER_CREATED_TIME, CLUSTER_UPDATED_TIME, CLUSTER_DELETED_TIME,
    CLUSTER_STATUS, CLUSTER_STATUS_REASON, CLUSTER_TIMEOUT,
    CLUSTER_METADATA,
) = (
    'name', 'profile_id', 'desired_capacity',
    'min_size', 'max_size', 'id', 'parent',
    'domain', 'project', 'user',
    'created_time', 'updated_time', 'deleted_time',
    'status', 'status_reason', 'timeout',
    'metadata',
)
