#!/bin/sh
mkdir -p etc/evoque
oslo-config-generator --output-file etc/evoque/evoque.conf \
                      --namespace evoque \
                      --namespace oslo.log \
