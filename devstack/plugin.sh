# evoque.sh - Devstack extras script to install evoque

# Save trace setting
XTRACE=$(set +o | grep xtrace)
set -o xtrace

echo_summary "evoque's plugin.sh was called..."
source $DEST/evoque/devstack/lib/evoque
(set -o posix; set)

if is_service_enabled sl-api sl-eng; then
    if [[ "$1" == "stack" && "$2" == "install" ]]; then
        echo_summary "Installing evoque"
        install_evoque
        #echo_summary "Installing evoqueclient"
        #install_evoqueclient
        cleanup_evoque
    elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
        echo_summary "Configuring evoque"
        configure_evoque

        if is_service_enabled key; then
            create_evoque_accounts
        fi

    elif [[ "$1" == "stack" && "$2" == "extra" ]]; then
        # Initialize evoque
        init_evoque

        # Start the evoque API and evoque taskmgr components
        echo_summary "Starting evoque"
        start_evoque
    fi

    if [[ "$1" == "unstack" ]]; then
        stop_evoque
    fi

    if [[ "$1" == "clean" ]]; then
        cleanup_evoque
    fi
fi

# Restore xtrace
$XTRACE
